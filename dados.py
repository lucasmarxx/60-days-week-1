import sqlite3
from gerador_dados import gera_dados_cliente, gera_dados_produtos, gera_dados_vendas, produtos_eletronicos


# banco1 = gera_dados_cliente('pt_BR', 500)
# banco1.gera_nomes()
# banco1.gera_emails()
# banco1.gera_telefone()

# dados_banco_1 = list(zip(banco1.lista_nomes, banco1.emails, banco1.lista_telefones))


# banco2 = gera_dados_produtos(produtos_eletronicos, 45)
# banco2.gera_produto()

# dados_banco_2 = banco2.lista_produtos

banco3 = gera_dados_vendas('banco_loja.db')


conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor()

# # cursor.execute(f"""
#                 CREATE TABLE IF NOT EXISTS clientes
#                 (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 telefone TEXT NOT NULL UNIQUE)
#                 """)

# cursor.execute(f"""
#                 CREATE TABLE IF NOT EXISTS produtos
#                 (id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 produto TEXT NOT NULL,
#                 preco_venda INTEGER NOT NULL,
#                 preco_custo INTEGER NOT NULL,
#                 estoque_atual INTEGER NOT NULL)
#                 """)

# cursor.execute(f"""
#                 CREATE TABLE IF NOT EXISTS vendas
#                 (id_venda INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 data_venda TEXT NOT NULL,
#                 id_cliente INTEGER,
#                 id_produto INTEGER,
#                 quantidade INTEGER NOT NULL,
#                 valor_total INTEGER NOT NULL,
#                 FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
#                 FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
#                 )
#                 """)

# cursor.execute('DELETE FROM vendas WHERE ')



if __name__ == '__main__':
#   cursor.executemany(
#      'INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)',
#      dados_banco_1)
#   print(f'{len(dados_banco_1)} colunas adicionadas')
    for _ in range(120):
        banco3.buscar_ids()
        banco3.gerar_datas()
        banco3.distribuir_vendas()
        cursor.executemany("""INSERT INTO vendas (data_venda, id_cliente, id_produto, quantidade, valor_total) VALUES (?, ?, ?, ?, ?)""",
                        [(banco3.data_formatada, banco3.id_cliente, banco3.id_produto, banco3.quantidade_venda, banco3.valor_total)])
    # cursor.execute('DROP TABLE IF EXISTS vendas')
    # cursor.execute('ALTER TABLE clientes RENAME COLUMN id TO id_clientes')

    # print(f'data venda: {banco3.data_formatada}, id do cliente: {banco3.id_cliente}, id do produto: {banco3.id_produto}, quantidade de vendas: {banco3.quantidade_venda}, valor total: {banco3.valor_total}')
    conexao.commit()
    conexao.close()