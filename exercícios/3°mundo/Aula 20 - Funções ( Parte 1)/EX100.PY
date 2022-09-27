from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0,10)
        lista.append(n)
        sleep(0.5)
        print(f'{n}', end=' ')
    print()
        
def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}',end=' ')
    sleep(0.3)
    print(f'obtemos o resultado {soma}')
            
    
    
num=list()
sorteia(num)

somaPar(num)