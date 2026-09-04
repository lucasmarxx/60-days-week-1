import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import pprint
from minha_key import chave
import sqlite3
from datetime import datetime


app = FastAPI()
chave_api = chave

@app.get('/get-data')
def requestar():
    resposta = requests.get('https://economia.awesomeapi.com.br/')
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {'erro': f'status: {resposta.status_code}'}

requesta_status = requestar()
pprint.pprint(requesta_status)

@app.get('/get-data')
def pegar_cotacao(moedas):
    resposta = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moedas}')
    return resposta.json()

cotacao_dolar = pegar_cotacao('USD-BRL')
cotacao_euro = pegar_cotacao('EUR-BRL')

valor_atual_dolar = cotacao_dolar['USDBRL']['bid']
valor_atual_euro = cotacao_euro['EURBRL']['bid']

conexao = sqlite3.connect('banco_cotacoes.db')
cursor = conexao.cursor()

# cursor.execute(f"""
#                 CREATE TABLE IF NOT EXISTS cotacoes
#                 (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 preco REAL,
#                 variacao REAL, 
#                 data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#                 """)
cursor.execute(f"""
                ALTER TABLE cotacoes ADD COLUMN moeda TEXT
""")
conexao.commit()
