from time import sleep
def contador(i, f, p):
    print('-='*20)
    print(f'Iniciando contagem de {i} para {f} de {p} em {p}')
    if i > f:
        while cont <= f:
            print(f'{cont}', end=' ')
            cont = 0
            cont += p
    else:



contador(1, 10, 2)
