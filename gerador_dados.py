import random
from faker import Faker
from context_manager_e_log import log_execucao

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

# gerar 3 tabelas (clientes, produtos, vendas) p/ fazer consultas complexas



class gera_dados_cliente:
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

class gera_dados_produtos:
    def __init__(self, produtos, qtd):
        self.produtos = produtos
        self.quantidade = qtd
        self.chaves = list(produtos)

    @log_execucao
    def gera_produto(self):
        self.lista_produtos = []
        for _ in range(self.quantidade):
            self.randomiza_estoque = random.randint(0, 105)
            self.chave_randomizada = self.chaves[random.randint(0, len(self.produtos) -1)]
            self.lista_produtos.append((self.chave_randomizada, self.produtos[self.chave_randomizada], self.randomiza_estoque))
        return self.lista_produtos

# dados_br = gera_dados_cliente('pt_BR', 20)

# dados_br.gera_nomes()
# dados_br.gera_emails()
# dados_br.gera_telefone()
# print(dados_br.lista_nomes)
# print('-----------.i.----------')

produtos1 = gera_dados_produtos(produtos_eletronicos, 80)
produtos1.gera_produto()
print(produtos1.lista_produtos, len(produtos1.lista_produtos))