print ('{:=^40}'.format('LOJA DA CAROL'))
preço = float(input('Valor da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção ? '))
if op == 1:
    total = preço - ( preço * 10 / 100 )
elif op == 2:
    total = preço - (preço * 5 /100 )
elif op == 3:
    total = preço 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif op == 4:
    total = preço + (preço * 20 / 100)
    totalp = int (input('Quantas parcelas? '))
    parcela = total / totalp
    print ('Sua compra será parcelada e em {}x de R${} no final.'.fomrat {preço, total})
else:
    print('Opção invalida de pagamento')
print('Sua compra de R${:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))