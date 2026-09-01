import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get('/get-data')
def testar_request():
    resposta = requests.get('https://economia.awesomeapi.com.br/')
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {'erro': f'status: {resposta.status_code}'}

teste = testar_request()
print(teste)

@app.get('get-data')
def testar_moeda(moeda):
    resposta = requests.get(f'https://economia.awesomeapi.com.br/json/last/:moedas, {moeda}')
    return resposta.json()
