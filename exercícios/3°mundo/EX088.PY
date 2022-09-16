from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 1
cont = 0
print ('--'*16)
print('       JOGA NA MEGA CENA       ')
print ('--'*16)
quant = int(input('Quantas jogadas você deseja? '))
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
while tot <= quant:
    while True:
        num = randint(1,60)
        if num not in lista: # IF para adiocionar somente números que não foram sorteados antes
            lista.append(num) 
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos): 
    print(f'jogo {i + 1}: {l}')
    sleep(1)
print('-='*4,'< BOA SORTE! >','-='*4)