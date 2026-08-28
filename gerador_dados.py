import random
import sqlite3
from faker import Faker
from context_manager_e_log import log_execucao
from datetime import datetime, timedelta

produtos_eletronicos = {
    'smartphone': 1500,
    'smart tv': 2300,
    'monitor': 500,
    'computador': 3500,
    'tablet': 1200,
    'caixa de som': 90,
    'fone de ouvido': 50,
    'carregador': 60,
    'echo dot': 150,
    'teclado': 60,
    'mouse': 60
}


class gerar_banco_vazio:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    @log_execucao
    def gera_banco(self):
        self.conexao = sqlite3.connect(f'{self.nome_banco}.db') #conecta ou cria um banco
        self.cursor = self.conexao.cursor()
        self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS clientes
                (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL UNIQUE)
                """)

        self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS produtos
                (id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                produto TEXT NOT NULL,
                preco_venda INTEGER NOT NULL,
                preco_custo INTEGER NOT NULL,
                estoque_atual INTEGER NOT NULL)
                """)

        self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS vendas
                (id_venda INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_venda TEXT NOT NULL,
                id_cliente INTEGER,
                id_produto INTEGER,
                quantidade INTEGER NOT NULL,
                valor_total INTEGER NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
                FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
                )
                """)
        self.conexao.commit()
        self.conexao.close()


# Gerar 3 tabelas (clientes, produtos, vendas) p/ fazer consultas complexas

# A função gera_dados_cliente recebe uma string, que será uma linguagem aceita pela biblioteca faker (exemplo: 'pt_BR'), 
# um número de nome de pessoas e um número que será o prefixo de telefone para essas pessoas.
# Após gerar os nomes das pessoas e o número, ela vai replicar um email para esses nomes e criará um número de telefone contendo
# o prefixo e nove números.

class gera_dados_cliente:
    def __init__(self, lingua: str, qtd: int, prefixo: int):
        self.prefixo = prefixo
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


    @log_execucao
    def gera_emails(self):
        self.emails = []
        for nome in self.lista_nomes:
            self.emails.append(f'{nome.lower()}@email.com')

    @log_execucao
    def gera_telefone(self):
        self.lista_telefones = []
        for nome in range(len(self.lista_nomes)):
            self.telefone = random.randint(923_400_030, 999_999_999)
            if f'(61){self.telefone}' not in self.lista_telefones:
                self.lista_telefones.append(f'({self.prefixo}){self.telefone}')
            else:
                self.telefone += 149
                self.lista_telefones.append(f'(61){self.telefone}')

    @log_execucao
    def gera_cliente(self):
        self.gera_nomes()
        self.gera_emails()
        self.gera_telefone()
        return self.lista_nomes, self.emails, self.lista_telefones


#A função gera_dados_produtos recebe um dicionário de produtos (neste caso, na variável produtos_eletronicos),
#e um valor inteiro que remete ao custo de cada item, calculada em base de %. exemplo: se passado
#o numero 40, então o custo de cada produto é 40% do valor deste item.

class gera_dados_produtos:
    def __init__(self, produtos, custo):
        self.produtos = produtos
        self.custo_padrao = custo
        self.chaves = list(produtos)
    
    @log_execucao
    def gera_produto(self):
        self.lista_produtos = []
        for nome, preco in self.produtos.items():
            self.estoque_randomizado = random.randint(25, 125)
            self.custo = round(preco * (self.custo_padrao * 0.01), 2) #custo = % do valor do preço
            self.dados = (nome, preco, self.custo, self.estoque_randomizado)
            self.lista_produtos.append(self.dados)

        return self.lista_produtos

#A função gera_dados_vendas recebe como parâmetro o seu próprio banco de dados feito, para inserção
#dos dados de venda.

class gera_dados_vendas:
    def __init__(self, banco_dados):
        self.banco_dados = banco_dados
        self.connection = sqlite3.connect(self.banco_dados)
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT id_clientes FROM clientes')
        self.clientes_ids = [row[0] for row in self.cursor.fetchall()]
        
        self.cursor.execute('SELECT id_produto, preco_venda FROM produtos')
        self.produtos = self.cursor.fetchall()
        self.produtos_ids = [row[0] for row in self.produtos]
        self.precos_produtos = {row[0]: row[1] for row in self.produtos}
    

    @log_execucao
    def gerar_datas(self):
        self.dt = datetime.now()
        self.data_fim = self.dt.date()
        self.data_inicio = self.data_fim - timedelta(days=180)

        self.dias_entre = (self.data_fim - self.data_inicio).days
        self.data_dias_entre = random.randint(0, self.dias_entre)
        self.data_venda = self.data_inicio + timedelta(days=self.data_dias_entre)
        self.data_formatada = self.data_venda.strftime('%Y-%m-%d')
        return self.data_formatada
    
    @log_execucao    
    def distribuir_vendas(self):
        self.id_cliente = random.choice(self.clientes_ids)
        self.id_produto = random.choice(self.produtos_ids)
        self.preco_venda = self.precos_produtos[self.id_produto]

        self.quantidade_venda = random.choices([1, 2, 3, 4], weights = [30, 20, 10, 5])[0]
        self.valor_total = self.preco_venda * self.quantidade_venda

        return self.id_cliente, self.id_produto, self.quantidade_venda, self.valor_total
    
if __name__ == '__main__':
    produtos1 = gera_dados_produtos(produtos_eletronicos, 45)
    produtos1.gera_produto()
    print(produtos1.lista_produtos, len(produtos1.lista_produtos))
    # conexao = sqlite3.connect('sqlite_db.db')
    # cursor = conexao.cursor()

    produtos = gera_dados_vendas('sqlite_db.db')
    # produtos.gerar_datas()
    # produtos.distribuir_vendas()

    # print(produtos.quantidade_venda)
    gerador_clientes_teste = gera_dados_cliente('es', 5, 11)
    # gerador_clientes_teste.gera_cliente()
    # print(gerador_clientes_teste.lista_nomes, gerador_clientes_teste.emails, gerador_clientes_teste.lista_telefones)
    teste = gerar_banco_vazio('banco_foda')
    teste.gera_banco()
