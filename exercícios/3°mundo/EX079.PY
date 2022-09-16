lista = []
while True:
    n=(int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor repetido, não irei adiociona-lo.')
    res=str(input('Deseja continuar ? [S/N] '))
    if res in 'Nn':
        break
print ('---'*30)
print(f'Você digitou os valores {sorted(lista)}')

