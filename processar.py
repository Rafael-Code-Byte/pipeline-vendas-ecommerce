import csv
from collections import defaultdict

def carregar_vendas(caminho):
    try:
        with open(caminho, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho}' não foi encontrado. Verifique o caminho e tente novamente.")
        return []

def total_por_categoria(vendas):
    totais = defaultdict(float)
    for venda in vendas:
        valor_total = float(venda['preco']) * int(venda['quantidade'])
        totais[venda['categoria']] += valor_total
    return totais

if __name__ == "__main__":
    vendas = carregar_vendas("data/vendas.csv")
    totais = total_por_categoria(vendas)
    for categoria, total in totais.items():
        print(f"{categoria}: R$ {total:.2f}")
