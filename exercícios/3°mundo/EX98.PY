from time import sleep

def contador(i, f, p):
    print(f'Iniciando contagem de {i} para {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont += p
        print('')
        print('=-' * 20)
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont -= p
        print('')
        print('=-' * 20)



# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez e personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
