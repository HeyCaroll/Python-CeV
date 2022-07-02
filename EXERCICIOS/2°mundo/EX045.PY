from random import randint
from time import sleep

itens  = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
x = int(input('Qual a sua escolha? '))

print ('-=-'*11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print ('-=-'*11)

print ('O jogador escolheu {}'.format(itens[x]))
print ('O computador escolheu {}'.format(itens[computador]))

if computador == 0:
    if x == 0:
        print('EMPATE')
    elif x == 1:
        print('O JOGADOR VENCEU')
    elif x == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if x == 0:
        print('O COMPUTAODR VENCEU')
    elif x == 1:
        print('EMPATE')
    elif x == 2:
        print ('O JOADOR VENCEU')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if x == 0:
        print('O JOGADOR VENCEU')
    elif x == 1:
        print('O COMPUTADOR VENCEU')
    elif x == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
