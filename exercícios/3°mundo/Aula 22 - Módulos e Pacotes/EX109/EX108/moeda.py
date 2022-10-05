def aumenta(num=0, formato=False):
    res=num + (num * 10/100)
    return res if formato is False else num


def diminuir(num=0, formato=False):
    res=num - (num * 13/100)
    return res if formato is False else num
    
    
def dobro(num=0, formato=False):
    res=num * 2
    return res if formato is False else num
    
    
def metade(num=0, formato=False):
    res=num / 2
    return res if formato is False else num


def resumo (valor, num, nume):
    print ('Aguarde, estamos realizando os calculos',end='')
for c in range(0,3):
    print('.', end ='', flush=True)
    sleep(0.8)
    
print()
print('~'* 40)

print(f'-> aumentando 10%, temos R${moeda.aumenta(valor, True)}')
print(f'-> Diminuindo 13% {valor} é {moeda.diminuir(valor)}')
print(f'-> O dobro de {valor} é {moeda.dobro(valor)}')
print(f'-> A metade de {valor} é {moeda.metade(valor)}'