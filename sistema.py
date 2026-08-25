class contaBancaria:
    def __init__(self, saldo: float, conta: int, id: str):
        self._saldo = saldo
        self._conta = conta
        self._id = id

        print(f'Bem vindo à sua conta: <{self._conta}>, id: {self._id}. Seu saldo é de R${self._saldo:.2f}.')

    def depositar(self, deposito):
        self._deposito = deposito
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

    def deposito_com_taxa(self, deposito, taxa):
        self._taxa_porcentagem = taxa
        self._taxa_do_deposito = deposito * (self._taxa_porcentagem * 0.01)
        self._deposito_com_taxa = deposito + self._taxa_do_deposito
        self._saldo += self._deposito_com_taxa

        print(f'Você depositou R${deposito:.2f} + taxa de {self._taxa_porcentagem}%. Total depositado: R${self._deposito_com_taxa:.2f}.')
        print(f'Valor da taxa: R${self._taxa_do_deposito:.2f}')
        print(f'Valor em saldo: R${self._saldo:.2f}.')

conta1 = contaBancaria(0, 33, 'lucas')
conta1.depositar(500)
conta1.sacar(230)
conta1.sacar(200)
conta1.sacar(69)
conta1.sacar(2)
print('#################################')
conta1.deposito_com_taxa(500,10)

conta2 = contaBancaria(232, 12, 'dandan')
conta2.deposito_com_taxa(2113, 3)
