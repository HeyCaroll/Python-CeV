from datetime import date
cont = 0
cont2 = 0
atual = date.today().year
for c in range(1,7):
    a1=int(input('Em que ano a {}° nasceu: '.format(c)))
    idade = atual - a1
    if idade >= 25:
        cont += 1
    else:
        cont2 += 1
print ('Ao total, temos {} pessoas maiores de idade e {} que ainda não atingiram a maioridade!'.format(cont, cont2))
