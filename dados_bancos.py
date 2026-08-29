import sqlite3
from gerador_dados import gera_dados_cliente, gera_dados_produtos, gera_dados_vendas


banco1 = gera_dados_cliente('pt_BR', 500, 11)
banco1.gera_cliente()

dados_banco_1 = list(zip(banco1.lista_nomes, banco1.emails, banco1.lista_telefones))
print(dados_banco_1)

banco3 = gera_dados_vendas('banco_loja.db')
banco3.gerar_datas()
banco3.distribuir_vendas()

dados_banco_3 = (banco3.data_formatada, banco3.id_cliente, banco3.id_produto, banco3.quantidade_venda, banco3.valor_total)



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
    conexao = sqlite3.connect('banco_loja.db')
    cursor = conexao.cursor()
    for _ in range(600):
        banco3.gerar_datas()
        banco3.distribuir_vendas()
        cursor.executemany("""INSERT INTO vendas (data_venda, id_cliente, id_produto, quantidade, valor_total) VALUES (?, ?, ?, ?, ?)""",
                        [(banco3.data_formatada, banco3.id_cliente, banco3.id_produto, banco3.quantidade_venda, banco3.valor_total)])
    conexao.commit()
    conexao.close()