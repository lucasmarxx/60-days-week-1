def log_execucao(funcao):
    def wrapper():
        funcao()
        with open('logs.log', 'a', encoding='utf8') as arquivo:
            arquivo.write(f'funcao {funcao.__name__} chamada.\n')
    return wrapper

@log_execucao
def funcao_teste():
    print('essa função é teste')

funcao_teste()