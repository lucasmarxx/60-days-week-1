import sqlite3
import random
from faker import Faker
from context_manager_e_log import log_execucao

conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor()

# gerar 3 tabelas (clientes, pedidos, itens) e fazer 10 consultas complexas



class gera_dados_usuario:
    def __init__(self, lingua, qtd):
        self.lingua = lingua
        self.quantidade = qtd

    @log_execucao
    def gera_nomes(self):
        self.lista_nomes = list()
        for i in range(self.quantidade):
            i = Faker(self.lingua)
            nome = i.name().split()

            if nome[0] != 'Dr.' and nome[0] != 'Srta.' and nome[0] != 'Sr.' and nome[0] != 'Sra.' and nome[0] != 'Dra.':
                self.lista_nomes.append(nome[0])
            else:
                self.lista_nomes.append(nome[1])

        return self.lista_nomes

    @log_execucao
    def gera_emails(self):
        self.emails = []
        for nome in self.lista_nomes:
            self.emails.append(f'{nome.lower()}@email.com')
        return self.emails    

    @log_execucao
    def gera_telefone(self):
        self.lista_telefones = []
        for nome in range(len(self.lista_nomes)):
            self.telefone = random.randint(923_400_030, 999_999_999)
            if f'(61){self.telefone}' not in self.lista_telefones:
                self.lista_telefones.append(f'(61){self.telefone}')
            else:
                self.telefone += 149
                self.lista_telefones.append(f'(61){self.telefone}')
        return self.lista_telefones, len(self.lista_telefones)


dados_br = gera_dados_usuario('pt_BR', 20)

dados_br.gera_nomes()
dados_br.gera_emails()
dados_br.gera_telefone()

print(dados_br.lista_nomes, dados_br.emails, dados_br.lista_telefones)

# # print(lista_br)
# print('------------------------------------------------------------------')
# # print(lista_emails_br)
# print('------------------------------------------------------------------')
# # print(lista_telefones)