cont = total = totmil = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print ('{:-^40}'.format(' \033[;1mFIM DO PROGRAMA\033[;m '))
print (f'O total de sua compra foi {total:.2f}')
print (f'Temos {totmil} produtos com o valor superior ao valor de R$1000.00')
print (f'O produto mais barato foi {barato}, que custa R${menor:.2f}')