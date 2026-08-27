import sqlite3
from gerador_dados import gera_dados_cliente, gera_dados_produtos

banco1 = gera_dados_cliente('pt_BR', 500)
banco1.gera_nomes()
banco1.gera_emails()
banco1.gera_telefone()

dados_banco_1 = list(zip(banco1.lista_nomes, banco1.emails, banco1.lista_telefones))

conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor()

# # cursor.execute(f"""
#                 CREATE TABLE IF NOT EXISTS clientes
#                 (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 telefone TEXT NOT NULL UNIQUE)
#                 """)





if __name__ == '__main__':
    cursor.executemany(
        'INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)',
        dados_banco_1)
    print(f'{len(dados_banco_1)} colunas adicionadas')
    conexao.commit()