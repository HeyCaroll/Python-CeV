def aumenta(num=0):
    return num + (num * (10/100))

    
def diminuir(num=0):
    return num - (num * (13/100))
    
    
def dobro(num=0):
    return num * 2
    
    
def metade(num=0):
    return num / 2


def moeda(p=0, m='R$'):
    return f'{m}{p:.1f}'.replace('.',',')