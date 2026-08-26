import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titular TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                numero TEXT NOT NULL UNIQUE
                )""")

# cursor.execute("""INSERT INTO contas_bancarias
#                 (titular, saldo, numero) VALUES
#                 ('vitao', 5400, '13234123')
                # """)

cursor.execute("""SELECT * FROM contas_bancarias""")
contas = cursor.fetchall()

for conta in contas:
    teste1, teste2, teste3, teste4 = conta
    print(f"""
id = {teste1},
titular = {teste2},
saldo = {teste3},
numero = {teste4}
""")
    

cursor.execute("""SELECT titular, saldo FROM contas_bancarias""" )
contas_novas = cursor.fetchall()

for conta in contas_novas:
    teste1, teste2 = conta
    print(f"""
titular: {teste1},
saldo: {teste2}""")

numero = int(input('digite o id desejado: '))

cursor.execute(f"""SELECT * FROM contas_bancarias WHERE id = {numero}""")

check_id = cursor.fetchall()


for info in check_id:
    info1, info2, info3, info4 = info
    print(f"""
Você selecionou o id {numero}, pertencente ao titular {info2}

dado1 = {info1},
dado2 = {info2},
dado3 = {info3},
dado4 = {info4}
""")


valor = int(input('digite um valor: '))
cursor.execute(f"""SELECT * FROM contas_bancarias WHERE saldo >= {valor}""")

check = cursor.fetchall()
for info in check:
    info1, info2, info3, info4 = info
    print(f"""
dado1 = {info1},
dado2 = {info2},
dado3 = {info3},
dado4 = {info4}
        """)

cursor.execute("""UPDATE contas_bancarias
                SET saldo = 3550
                WHERE id = 1 
                """)

# cursor.execute('DELETE FROM contas_bancarias WHERE ') #WHERE id = 1 <exemplo>

conexao.commit()