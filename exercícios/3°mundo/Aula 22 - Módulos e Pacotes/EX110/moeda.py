from time import sleep
import moeda
def aumenta(num=0, formato=False):
    res=num + (num * 10/100)
    return res if formato is False else moeda(res)


def diminuir(num=0, formato=False):
    res=num - (num * 13/100)
    return res if formato is False else moeda(res)
    
    
def dobro(num=0, formato=False):
    res=num * 2
    return res if formato is False else moeda(res)
    
    
def metade(num=0, formato=False):
    res=num / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')


def resumo (valor=0, TaxaA=10, TaxaR=5):
    print ('Aguarde, estamos realizando os calculos',end='')
    for c in range(0,3):
        print('.', end ='', flush=True)
        sleep(0.8)
    
    print()
    print('-='* 15)
    print('RESUMO DO VALOR'.center(30))
    print('-='* 15)
    print(f'Preço analisado \t{moeda(valor)}')
    print(f'-> {TaxaA}% de aumento: \t{aumenta(valor, True)}')
    print(f'-> {TaxaR}% de redução: \t{diminuir(valor,True)}')
    print(f'-> Dobro do preço: \t{dobro(valor, True)}')
    print(f'-> Metade do preço: \t{metade(valor,True)}' )
    print('-='* 15)
    