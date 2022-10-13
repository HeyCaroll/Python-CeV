def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mErro: Digite um número INTEIRO válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print(f'\033[31mErro: Digite um número REAL válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n