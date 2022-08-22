from operator import itemgetter
from random import randint
from time import sleep
print('-=- Valores sorteados -=-')
lista = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
for k,v in lista.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ordem = sorted(lista.items(),key=itemgetter(1), reverse=True)
print('-='*15)
for c,v in enumerate(ordem):
    print(f'{c+1} lugar: {v[0]} com {v[1]}')
    sleep(1)

