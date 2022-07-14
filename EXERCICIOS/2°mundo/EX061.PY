print('-=-'*10)
print('*       GERADOR DE P.A        *')
print('-=-' * 10)
n1 = int(input('Digite um núemro: '))
razão = int(input('Digite uma razão: '))
cont = 1
while cont < 10:
    print('{} → '.format(n1), end='')
    n1 += razão
    cont += 1
print('FIM')
