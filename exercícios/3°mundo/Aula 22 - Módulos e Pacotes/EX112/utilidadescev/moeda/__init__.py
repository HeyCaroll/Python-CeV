def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):

    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0.00, valor_da_moeda='R$'):
    return f'{valor_da_moeda} {preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa_a=0, taxa_d=0):
    print('-' * 30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('-' * 30)
    print('\033[m', end='')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preco, taxa_a, True)}')
    print(f'{taxa_d}% de redução: \t{diminuir(preco, taxa_d, True)}')
    print('-' * 30)