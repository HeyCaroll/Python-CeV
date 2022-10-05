def escreva(txt):
    print('=' * (len(txt) + 2))
    print(f' {txt}')
    print('=' * (len(txt) + 2))


def ajuda(msg):
    print('\033[1;30;45m', end='')
    escreva(f'Acessando o manual do comando <<<"{msg}">>>')
    print('\033[1;31;40m', end='')
    from time import sleep
    sleep(1)
    help(msg)


# Programa Principal
while True:
    print('\033[1;30;44m', end='')
    escreva('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')
    comando = str(input('Função ou Biblioteca: ')).lower().strip()
    if comando == 'fim':
        print('\033[1;30;41m-PROGRAMA ENCERRADO-')
        break
    else:
        ajuda(comando)
        print('\033[m', end='')