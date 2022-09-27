print('-=-'*10)
print('*       GERADOR DE P.A        *')
print('-=-' * 10)
n1 = int(input('Primeiro termo: '))
razão = int(input('Digite uma razão: '))
termo = n1
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int (input('Qantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
