from sistema import contaBancaria, contaSalario

conta1 = contaBancaria(0, 11, 'luquinhas')
conta1.depositar_com_taxa(532, 11)

conta2 = contaSalario(5000, 12, 'bibito')
conta2.saque_com_bonus(450, 2)


def meu_decorator(funcao_decorator):
    def wrapper(arg1, arg2):
        print('Primeiro print do wrapper')
        funcao_decorator(arg1, arg2)
        print('Segundo print do wrapper')
    return wrapper


@meu_decorator
def pegar_saldo(num1, num2):
    saldo_anterior = conta2._saldo 
    novo_saldo = saldo_anterior + (num1 + num2)
    print(f'{novo_saldo} = ({saldo_anterior} + {num1} + {num2})')

pegar_saldo(150, 130)

@meu_decorator
def funcao_teste(argx, argy):
    print(f'primeiro argumento: {argx}, segundo argumento: {argy}')

funcao_teste('macaco', 'golira')