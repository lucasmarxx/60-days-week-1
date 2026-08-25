class usuario:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def dados_usuario(self):
        self.contaBancaria = contaBancaria()

class contaBancaria:
    def __init__(self, saldo: float, conta: int, id: str):
        self._saldo = saldo
        self._conta = conta
        self._id = id.capitalize()

        print(f'Bem vindo à sua conta: <{self._conta}>, id: {self._id}. Seu saldo é de R${self._saldo:.2f}.')
        print('------')

    def depositar(self, deposito):
        self._deposito = deposito
        self._saldo += deposito
        print(f'Deposito de R${deposito:.2f} na conta <{self._conta}>.')
        print(f'Novo saldo: R${self._saldo:.2f}')
        print('------')

    def sacar(self, saque):
        self.saque = saque
        if self._saldo >= saque:
            self._saldo -= saque
            print(f'Saque de R${saque:.2f} na conta <{self._conta}>.')
            print(f'Novo saldo da conta numero <{self._conta}> em nome de <{self._id}>: R${self._saldo:.2f}.')
            print('------')
        else:
            print(f'Falha na tentativa de sacar R${saque:.2f}. Saldo em conta: R${self._saldo:.2f}.')
            print('nao tem dinheiro fdp vai toma no seu cu')
            print('------')

    def depositar_com_taxa(self, deposito, taxa):
        self._taxa_deposito = deposito * (taxa * 0.01)
        self._deposito_com_taxa = deposito - self._taxa_deposito
        self._saldo += self._deposito_com_taxa

        print(f'Você depositou R${deposito:.2f}. Foi cobrada taxa de {taxa}%. Total depositado: R${self._deposito_com_taxa:.2f}.')
        print(f'Taxa: {taxa}%. Valor da taxa: R${self._taxa_deposito:.2f}')
        print(f'Valor em saldo: R${self._saldo:.2f}.')
        print('------')
    def saque_com_bonus(self, saque, bonus):
        self._bonus_saque = saque * (bonus * 0.01)
        self._saque_com_bonus = saque + self._bonus_saque
        if self._saldo >= saque:
            self._saldo -= self._saque_com_bonus
            print(f'Valor do saque: R${saque:.2f}. Valor do bonus de {bonus}% no saque: R${self._bonus_saque:.2f}.')
            print('------')
        else:
            print(f'Saldo insuficiente para saque. Saldo: R${self._saldo:.2f}. vai toma no seu cu')
            print('------')

#conta com restrição de depósito, apenas saque

class contaSalario(contaBancaria):
    def __init__(self, saldo, conta, id):
        self._saldo = saldo
        self._conta = conta
        self._id = id

    def sacar(self, saque):
        if self._saldo >= saque:
            self._saldo -= saque
            print(f'Saque de R${saque:.2f} realizado.')
            print(f'Saldo disponível na conta salário: R${self._saldo:.2f}.')
        else:
            print(f'Impossível sacar R${saque:.2f}. Valor em conta: R${self._saldo:.2f}.')
        
    def depositar(self, deposito=None):
        raise NotImplementedError('Impossível depositar na conta salário, seu merda')
    
    def saque_com_bonus(self, saque, bonus):
        return super().saque_com_bonus(saque, bonus)
    
    
conta1 = contaBancaria(0, 33, 'lucas')
conta1.depositar(500)
conta1.sacar(230)
conta1.sacar(200)
conta1.sacar(69)
conta1.sacar(2)
conta1.depositar_com_taxa(500,10)

conta2 = contaBancaria(232, 12, 'dandan')
conta2.depositar_com_taxa(2113, 3)
conta2.sacar(422)
conta2.depositar_com_taxa(302, 3)
conta2.saque_com_bonus(300, 10)

salario1 = contaSalario(312, 2, 'luquinhas')
salario1.sacar(55)
# salario1.depositar(22)
salario1.saque_com_bonus(135, 10)