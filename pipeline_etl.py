import csv
import psycopg2

def extrair(caminho):
    with open(caminho, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def carregar(vendas):
    conn = psycopg2.connect(dbname="ecommerce_db", user="rafael")
    cur = conn.cursor()
    for venda in vendas:
        cur.execute(
            "INSERT INTO vendas_diarias (produto, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
            (venda['produto'], venda['categoria'], float(venda['preco']), int(venda['quantidade']))
        )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    vendas = extrair("data/vendas.csv")
    carregar(vendas)
    print(f"{len(vendas)} registros carregados na tabela vendas_diarias.")
