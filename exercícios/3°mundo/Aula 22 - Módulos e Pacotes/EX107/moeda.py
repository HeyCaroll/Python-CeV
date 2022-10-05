def aumenta(num):
    return num + (num * 10/100)

    
    
def diminuir(num):
    return num - (num * 13/100)
    
    
def dobro(num):
    return num * 2
    
    
def metade(num):
    return num / 2


def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.',',')