import sqlite3
conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor()

consulta_1 = """    
    SELECT 
        c.nome AS cliente,
        COUNT(v.id_venda) AS total_pedidos,
        SUM(v.valor_total) AS total_gasto
    FROM clientes c
    INNER JOIN vendas v ON c.id_clientes = v.id_cliente
    INNER JOIN produtos p ON p.id_produto = v.id_produto
    WHERE v.data_venda >= '2026-01-01'
    GROUP BY c.id_clientes, c.nome
    HAVING total_gasto > 600.00 and total_gasto < 25000.00
    ORDER BY total_gasto DESC;
"""

consulta_2 = """
    SELECT
        p.produto AS nome_produto,
        SUM(v.quantidade) AS total_vendido
    FROM vendas v
    INNER JOIN produtos p ON v.id_produto = p.id_produto
    WHERE v.data_venda >= '2026-01-01'
    GROUP BY p.id_produto, p.produto
    ORDER BY total_vendido DESC;

    """

consulta_3 = """
    SELECT
        c.nome AS cliente,
        COUNT(v.id_venda) AS total_pedidos,
        SUM(v.valor_total) AS total_gasto
    FROM clientes c
    INNER JOIN vendas v ON c.id_clientes = v.id_cliente
    WHERE v.data_venda >= DATE('now', '-3 months')
    GROUP BY c.id_clientes, c.nome
    ORDER BY total_gasto DESC;

"""

# corrigir datas para formato universal
# query_conversao = """
#     UPDATE vendas
#     SET data_venda = 
#         SUBSTR(data_venda, 7, 4) || '-' ||
#         SUBSTR(data_venda, 4, 2) || '-' ||
#         SUBSTR(data_venda, 1, 2) 
#     WHERE data_venda LIKE '__/__/____';
# """

# cursor.execute(query_conversao)

# cursor.execute(consulta_1)
# cursor.execute(consulta_2)
cursor.execute(consulta_3)

resultados = cursor.fetchall()

# checagem formato de datas
# cursor.execute('SELECT data_venda FROM vendas LIMIT 5;')
# print(cursor.fetchall())

# resultado consulta 1
# print(f"{'Cliente': <20} | {'Pedidos': <8} | {'Total Gasto': <12}")
# print('-' * 45)
# for linha in resultados:
#     nome, pedidos, total = linha
#     print(f'{nome:<20} | {pedidos:<8} | R$ {total:>10.2f}')

# resultado consulta 2
# print(f"{'Produto': <25} | {'qtd vendida':<12}")
# print('-' * 40)
# for linha in resultados:
#     produto, qtd = linha
#     qtd_val = qtd if qtd is not None else 0
#     print(f'{produto:<25} | {qtd_val:<12}')

print(f"{'Cliente':<20} | {'Pedidos':<8} | {'Total Gasto':<12}")
print('-' * 53)
for linha in resultados:
    nome, pedidos, total = linha
    print(f'{nome:<25} | {pedidos:<8} | R$ {total:.2f}')
print(len(resultados))

conexao.close()