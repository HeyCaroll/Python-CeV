totm = toth = tot18 = 0
while True:
    print('\033[1;90m---\033[m'*10)
    print('\033[;1m   CADASTRE UMA PESSOA\033[;m')
    print('\033[1;90m---\033[m'*10)
    i = int(input('Idade: '))
    if i > 18:
        tot18 +=1
    s = ' '
    while s not in 'FM':
        s = str(input('Sexo: [M/F]')).upper()
    if s == 'F' and i <= 20:
        totm +=1
    if s == 'M':
        toth += 1
    c = ' '
    while c not in 'SN':   
        c = str(input('Deseja continuar? [S/N] ')).upper()
    if c == 'N':
        break
print('\033[1;90m---\033[m'*10)
print(f'Quantas pessoas tem mais de 18 anos: {tot18}.')
print(f'Quantidade de homens cadrastados {toth}.')
print(f'Quantidade de mulheres com menos de 20 anos {totm}.')