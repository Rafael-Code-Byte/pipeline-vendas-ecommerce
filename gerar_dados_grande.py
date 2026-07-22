import csv
import random

categorias = ['Eletronicos', 'Papelaria', 'Acessorios', 'Alimentos', 'Vestuario']
produtos_por_categoria = {
    'Eletronicos': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Fone de Ouvido'],
    'Papelaria': ['Caderno', 'Caneta', 'Lapis', 'Borracha', 'Agenda'],
    'Acessorios': ['Mochila', 'Carteira', 'Relogio', 'Oculos', 'Cinto'],
    'Alimentos': ['Cafe', 'Chocolate', 'Biscoito', 'Suco', 'Barra de Cereal'],
    'Vestuario': ['Camiseta', 'Calca', 'Jaqueta', 'Bone', 'Meia'],
}

with open('data/vendas_grande.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['produto', 'categoria', 'preco', 'quantidade'])
    for _ in range(500_000):
        categoria = random.choice(categorias)
        produto = random.choice(produtos_por_categoria[categoria])
        preco = round(random.uniform(5, 3000), 2)
        quantidade = random.randint(1, 20)
        writer.writerow([produto, categoria, preco, quantidade])

print("Arquivo gerado: data/vendas_grande.csv")
