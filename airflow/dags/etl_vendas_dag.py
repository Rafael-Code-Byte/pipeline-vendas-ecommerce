import csv
from datetime import datetime
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
import psycopg2


def extrair(**context):
    with open("/opt/airflow/data/vendas.csv", newline='', encoding='utf-8') as f:
        vendas = list(csv.DictReader(f))
    context['ti'].xcom_push(key='vendas', value=vendas)


def carregar(**context):
    vendas = context['ti'].xcom_pull(key='vendas', task_ids='extrair_dados')
    conexao = BaseHook.get_connection('postgres_ecommerce')

    conn = psycopg2.connect(
        dbname=conexao.schema,
        user=conexao.login,
        password=conexao.password,
        host=conexao.host,
        port=conexao.port,
    )
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE vendas_diarias;")
    for venda in vendas:
        cur.execute(
            "INSERT INTO vendas_diarias (produto, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
            (venda['produto'], venda['categoria'], float(venda['preco']), int(venda['quantidade']))
        )
    conn.commit()
    cur.close()
    conn.close()


with DAG(
    dag_id="etl_vendas_dag",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extrair_dados = PythonOperator(
        task_id="extrair_dados",
        python_callable=extrair,
    )

    carregar_dados = PythonOperator(
        task_id="carregar_dados",
        python_callable=carregar,
    )

    disparar_databricks = DatabricksRunNowOperator(
        task_id="disparar_databricks",
        databricks_conn_id="databricks_default",
        job_id="615053155279694",
    )	


    extrair_dados >> carregar_dados >> disparar_databricks
