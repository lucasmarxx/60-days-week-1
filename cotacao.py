import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import pprint
from minha_key import chave
import sqlite3
# import schedule
from datetime import datetime, timedelta
import time
from log import log_execucao

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
# pprint.pprint(requesta_status)

@app.get('/get-data')
def pegar_cotacao(moedas):
    resposta = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moedas}')
    return resposta.json()

cotacao_dolar = pegar_cotacao('USD-BRL')
cotacao_euro = pegar_cotacao('EUR-BRL')

# pprint.pprint(cotacao_dolar)

dados_dolar = cotacao_dolar['USDBRL']
dados_euro = cotacao_euro['EURBRL']


# pprint.pprint(dados_dolar)
# print(add_dados_dolar)

# ordem na tabela:
# name => nome
# bid => preco
# pctchange => variacao
# code => moeda

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
# cursor.execute(f"""
#                 ALTER TABLE cotacoes ADD COLUMN moeda TEXT
# """)

@log_execucao
def adiciona_cotacao_dolar(dados):
    cursor.executemany(f"""
                    INSERT INTO cotacoes (nome, preco, variacao, moeda) VALUES (?, ?, ?, ?)
                    """, [(dados['name'], float(dados['bid']), float(dados['pctChange']), dados['code'])])
    conexao.commit()

@log_execucao
def adiciona_cotacao_euro(dados):
    cursor.executemany(f"""
                    INSERT INTO cotacoes (nome, preco, variacao, moeda) VALUES (?, ?, ?, ?)
                    """, [(dados['name'], float(dados['bid']), float(dados['pctChange']), dados['code'])])
    conexao.commit()

hora_limite = 19
proxima_execucao = datetime.now()

while True:
    agora = datetime.now()
    if agora.hour >= hora_limite:
        print('Deu a hora, encerrando adição de cotações!')
        break

    if agora >= proxima_execucao:
        adiciona_cotacao_dolar(dados_dolar)
        adiciona_cotacao_euro(dados_euro)
        proxima_execucao = agora + timedelta(minutes=10)
        print(f'Cotações adicionadas. Próxima execução: {proxima_execucao.strftime('%H:%M:%S')}')

    time.sleep(1)
