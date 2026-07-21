import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipeline_etl import extrair, calcular_valor

def test_calcular_valor():
    venda = {'preco': '10.00', 'quantidade': '3'}
    assert calcular_valor(venda) == 30.0

def test_extrair(tmp_path):
    csv_content = "produto,categoria,preco,quantidade\nCaneta,Papelaria,2.50,4\n"
    arquivo = tmp_path / "teste.csv"
    arquivo.write_text(csv_content, encoding="utf-8")
    resultado = extrair(str(arquivo))
    assert len(resultado) == 1
    assert resultado[0]['produto'] == 'Caneta'
