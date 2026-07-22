from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def diz_ola():
    print("Olá! Meu primeiro DAG do Airflow está funcionando.")

with DAG(
    dag_id="meu_primeiro_dag",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    tarefa_ola = PythonOperator(
        task_id="dizer_ola",
        python_callable=diz_ola,
    )
