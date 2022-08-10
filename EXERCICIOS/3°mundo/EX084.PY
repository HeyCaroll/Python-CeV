pes = []
mai = men = 0
list = []
while True:
    pes.append(str(input(' informe o seu nome: ')))
    pes.append(float(input('informe o seu peso: ')))
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
print (f'Ao total temos {len(list)} pessoas cadrastadas')
print(f'O maior peso foi {mai}')
print(f'O menor peso foi {men}')
