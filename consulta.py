import sqlite3
conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor()

consulta = """    
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


cursor.execute(consulta)

resultados = cursor.fetchall()

print(f"{'Cliente': <20} | {'Pedidos': <8} | {'Total Gasto': <12}")
print('-' * 45)
for linha in resultados:
    nome, pedidos, total = linha
    print(f'{nome:<20} | {pedidos:<8} | R$ {total:>10.2f}')

conexao.close()