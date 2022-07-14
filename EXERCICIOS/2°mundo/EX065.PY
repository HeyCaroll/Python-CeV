r = 'S'
soma = media = maior = menor = cont= 0
while r in 'Ss':
    n = int(input('digite um número:'))
    soma +=n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = num
    r = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]
media = soma / cont
print ('Você digitou {} números e a média foi {}'.format(cont, media))
print ('O maior valor foi {} e o menor foi {}'.format(maior, menor))
