class contaBancaria:
    def __init__(self, saldo: float, conta: int, id: str):
        self._saldo = saldo
        self._conta = conta
        self._id = id

        print(f'Bem vindo à sua conta: <{self._conta}>, id: {self._id}. Seu saldo é de R${self._saldo:.2f}.')

    def depositar(self, deposito):
        self.deposito = deposito
        self._saldo += deposito
        print(f'Deposito de R${deposito:.2f} na conta <{self._conta}>.')
        print(f'Novo saldo: R${self._saldo:.2f}')

    def sacar(self, saque):
        self.saque = saque
        if self._saldo >= 0 and self._saldo >= saque:
            self._saldo -= saque
            print(f'Saque de R${saque:.2f} na conta <{self._conta}>.')
            print(f'Novo saldo da conta numero <{self._conta}> em nome de <{self._id}>: R${self._saldo:.2f}.')
        else:
            print(f'Falha na tentativa de sacar R${saque:.2f}. Saldo em conta: R${self._saldo:.2f}.')
            print('nao tem dinheiro fdp vai toma no seu cu')



conta1 = contaBancaria(0, 33, 'lucas')
conta1.depositar(500)
conta1.sacar(230)
conta1.sacar(200)
conta1.sacar(69)
conta1.sacar(2)