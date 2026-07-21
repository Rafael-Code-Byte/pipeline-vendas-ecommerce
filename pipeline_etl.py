import csv
import logging
import psycopg2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def extrair(caminho):
    logging.info(f"Extraindo dados de {caminho}")
    with open(caminho, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def calcular_valor(venda):
    return float(venda['preco']) * int(venda['quantidade'])

def carregar(vendas):
    conn = psycopg2.connect(dbname="ecommerce_db", user="rafael")
    cur = conn.cursor()
    for venda in vendas:
        cur.execute(
            "INSERT INTO vendas_diarias (produto, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
            (venda['produto'], venda['categoria'], calcular_valor(venda) / int(venda['quantidade']), venda['quantidade'])
        )
    conn.commit()
    cur.close()
    conn.close()
    logging.info(f"{len(vendas)} registros carregados na tabela vendas_diarias.")

if __name__ == "__main__":
    vendas = extrair("data/vendas.csv")
    carregar(vendas)
