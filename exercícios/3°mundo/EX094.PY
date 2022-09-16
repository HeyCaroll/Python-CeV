dados = dict()
ficha = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Genero: [M/F]')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print(' \033[1;31mERRO! Por favor, digite apenas M ou F.\033[m')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    ficha.append(dados.copy())
    while True:
        res = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if res in 'SN':
            break
        print('	\033[1;31mERRO! por favor, digite apensa S ou N.\033[m')
    if res == 'N':
        break
print(f'Ao total temos {len(ficha)} pessoas cadrastadas.')
media = soma / len(ficha)
print (f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadrastadas foram', end='')
for p in ficha:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'Lista das pessoas acima da media:', end='')
for p in ficha:
    if p['idade'] >= media:
        print(' ',end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<<PROGRAMA ENCERRADO>>')

