from context_manager_e_log import log_execucao
import sqlite3


class usuario:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def dados_usuario(self):
        self.contaBancaria = contaBancaria(300, 15, 'bibito')

class contaBancaria:
    def __init__(self, saldo: float, conta: int, id: str):
        self._saldo = saldo
        self._conta = conta
        self._id = id.capitalize()

        print(f'Bem vindo à sua conta: <{self._conta}>, id: {self._id}. Seu saldo é de R${self._saldo:.2f}.')
        print('------')
    @log_execucao
    def depositar(self, deposito):
        self._saldo += deposito
        print(f'Valor em saldo: R${self._saldo:.2f}.')
        print(f'Deposito de R${deposito:.2f} na conta <{self._conta}>.')
        print(f'Novo saldo: R${self._saldo:.2f}')
        print('------')
    @log_execucao
    def sacar(self, saque):
        self.saque = saque
        if self._saldo >= saque:
            self._saldo -= saque
            print(f'Valor em saldo: R${self._saldo:.2f}.')
            print(f'Saque de R${saque:.2f} na conta <{self._conta}>.')
            print(f'Novo saldo da conta numero <{self._conta}> em nome de <{self._id}>: R${self._saldo:.2f}.')
            print('------')
        else:
            print(f'Falha na tentativa de sacar R${saque:.2f}. Saldo em conta: R${self._saldo:.2f}.')
            print('nao tem dinheiro fdp vai toma no seu cu')
            print('------')

    @log_execucao
    def depositar_com_taxa(self, deposito, taxa):
        self._taxa_deposito = deposito * (taxa * 0.01)
        self._deposito_com_taxa = deposito - self._taxa_deposito
        print(f'Valor em saldo: R${self._saldo:.2f}.')
        self._saldo += self._deposito_com_taxa
        
        print(f'Você depositou R${deposito:.2f}. Foi cobrada taxa de {taxa}%. Total depositado: R${self._deposito_com_taxa:.2f}.')
        print(f'Taxa: {taxa}%. Valor da taxa: R${self._taxa_deposito:.2f}')
        print(f'Valor em saldo: R${self._saldo:.2f}.')
        print('------')
    @log_execucao    
    def saque_com_bonus(self, saque, bonus):
        self._bonus_saque = saque * (bonus * 0.01)
        self._saque_com_bonus = saque + self._bonus_saque
        if self._saldo >= saque:
            print(f'Valor em conta: R${self._saldo:.2f}')
            self._saldo -= self._saque_com_bonus
            print(f'Valor do saque: R${saque:.2f}. Valor do bonus de {bonus}% no saque: R${self._bonus_saque:.2f}.')
            print(f'Valor em conta: R${self._saldo:.2f}.')
            print('------')
        else:
            print(f'Saldo insuficiente para saque. Saldo: R${self._saldo:.2f}. vai toma no seu cu')
            print('------')

    @log_execucao
    def conectar_banco(self):
        self.conexao = sqlite3.connect('sqlite_db.db')
        self.cursor = self.conexao.cursor()
        # self.conexao.commit()
    @log_execucao
    def adicionar_dados_db(self):
        self.cursor.execute(f"""INSERT INTO contas_bancarias
                        (titular, saldo, numero) VALUES
                        ('{self._id}', {self._saldo:.2f}, '{self._conta}')""")
        self.conexao.commit()
#conta com restrição de depósito, apenas saque

class contaSalario(contaBancaria):
    def __init__(self, saldo, conta, id):
        self._saldo = saldo
        self._conta = conta
        self._id = id.capitalize()
    @log_execucao
    def sacar(self, saque):
        return super().sacar(saque)
    @log_execucao
    def depositar(self, deposito=None):
        raise NotImplementedError('Impossível depositar na conta salário, seu merda')
    @log_execucao
    def saque_com_bonus(self, saque, bonus):
        return super().saque_com_bonus(saque, bonus)
    

if __name__ == '__main__':
    conta1 = contaBancaria(0, 33, 'lucas')
    conta1.depositar(500)
    conta1.sacar(230)
    conta1.sacar(200)
    conta1.sacar(69)
    conta1.sacar(2)
    conta1.depositar_com_taxa(500,10)
    # conta1.conectar_banco()
    # conta1.adicionar_dados_db()

    conta2 = contaBancaria(232, 12, 'dandan')
    conta2.depositar_com_taxa(2113, 3)
    conta2.sacar(422)
    conta2.depositar_com_taxa(302, 3)
    conta2.saque_com_bonus(300, 10)
    # conta2.conectar_banco()
    # conta2.adicionar_dados_db()

    salario1 = contaSalario(312, 2, 'luquinhas')
    salario1.sacar(55)
    # salario1.depositar(22)
    salario1.saque_com_bonus(135, 10)
    # salario1.conectar_banco()
    # salario1.adicionar_dados_db()

    conta3 = contaBancaria(8000, 55, 'bibito')
    conta3.depositar_com_taxa(350, 3)
    conta3.saque_com_bonus(220, 10)
    conta3.conectar_banco()
    conta3.adicionar_dados_db()