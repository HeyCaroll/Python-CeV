import moeda
from time import sleep

valor = float(input('\033[1;34mDigite o valor: R$ \033[m'))
print ('Aguarde, estamos realizando os calculos',end='')
for c in range(0,3):
    print('.', end ='', flush=True)
    sleep(0.8)
    
print()
print('~'* 40)

print(f'-> A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'-> O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'-> aumentando 10%, temos {moeda.moeda(moeda.aumenta(valor))}')
