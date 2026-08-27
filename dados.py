import sqlite3
from gerador_dados import gera_dados_cliente, gera_dados_produtos, produtos_eletronicos


banco1 = gera_dados_cliente('pt_BR', 500)
banco1.gera_nomes()
banco1.gera_emails()
banco1.gera_telefone()

banco2 = gera_dados_produtos(produtos_eletronicos, 500)
banco2.gera_produto()

dados_banco_1 = list(zip(banco1.lista_nomes, banco1.emails, banco1.lista_telefones))
dados_banco_2 = banco2.lista_produtos


conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor()

# # cursor.execute(f"""
#                 CREATE TABLE IF NOT EXISTS clientes
#                 (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 telefone TEXT NOT NULL UNIQUE)
#                 """)

cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS produtos
                (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                produto TEXT NOT NULL,
                valor INTEGER NOT NULL,
                estoque INTEGER NOT NULL)
                """)



if __name__ == '__main__':
#   cursor.executemany(
#      'INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)',
#      dados_banco_1)
#   print(f'{len(dados_banco_1)} colunas adicionadas')
    cursor.executemany('INSERT INTO produtos (produto, valor, estoque) VALUES (?, ?, ?)',
                        dados_banco_2)
    conexao.commit()