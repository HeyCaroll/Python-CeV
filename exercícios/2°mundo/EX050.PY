soma = 0
cont = 0
for c in range (1,7):
    x=int(input('Digite o {}° número: '.format(c)))
    if x % 2 == 0:
        soma += x
        cont += 1
print ('\033[1;37mVocê informou {} números pares e a soma foi {} !\033[m'.format(cont, soma))


