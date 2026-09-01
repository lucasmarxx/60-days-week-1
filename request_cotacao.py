import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get('/get-data')
def pegar_cotacao():
    resposta = requests.get('https://economia.awesomeapi.com.br/')
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {'erro': f'status: {resposta.status_code}'}

teste = pegar_cotacao()
print(teste)