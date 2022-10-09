import moeda
from time import sleep

valor = float(input('\033[1;34mDigite o valor: R$ \033[m'))

print ('Aguarde, estamos realizando os calculos',end='')
for c in range(0,3):
     print('.', end ='', flush=True)
     sleep(0.4)
    
print()
print('~'* 40)
print(f'-> aumentando 10%, temos {moeda.aumenta(valor,10, True)}')
print(f'-> Diminuindo 13% {valor}, temos {moeda.diminuir(valor,13,True)}')
print(f'-> O dobro de {valor} é {moeda.dobro(valor,True)}')
print(f'-> A metade de {valor} é {moeda.metade(valor,True)}')
 