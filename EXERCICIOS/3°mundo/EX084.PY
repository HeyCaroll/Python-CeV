pes = []
list = []
mai = men = 0
while True:
    pes.append(str(input('Informe o seu nome: ')))
    pes.append(float(input('Informe o seu peso: ')))
    if len(list) == 0:
        mai = men = pes [1]
    else:
        if pes[1] > mai:
            mai = pes[1]
        if pes[1] < men:
            men = pes[1]
    list.append(pes[:])
    pes.clear()
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if res == 'N':
        break
print('-=-' * 30)
print (f'Ao total temos {len(list)} pessoas cadastradas')
print(f'O maior peso foi de {mai}, pertencendo a ', end='')
for p in list:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men} kg. Peso de ', end='')
for p in list:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
