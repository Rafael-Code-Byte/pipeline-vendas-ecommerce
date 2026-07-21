import psycopg2

conn = psycopg2.connect(dbname="ecommerce_db", user="rafael")
cur = conn.cursor()

cur.execute("""
    SELECT pr.categoria, SUM(pr.preco * ip.quantidade) AS total_receita
    FROM itens_pedido ip
    JOIN produtos pr ON ip.produto_id = pr.id
    GROUP BY pr.categoria;
""")

for categoria, total in cur.fetchall():
    print(f"{categoria}: R$ {total:.2f}")

cur.close()
conn.close()
