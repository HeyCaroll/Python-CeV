somaidade = 0
media = 0
nomev = 0
idadev = 0
totM = 0

for c in range(1,5):
    print('------ {}° PESSOA -----'.format(c))
    nome = str(input('Qual é o seu nome: ')).strip()
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Qual é o seu genero [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        idadev = idade
        nomev = nome
    if sexo in 'Mm' and idade > idadev:
        idadev = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        totM += 1


media = somaidade / 4
print ('A média de idade do grupo é de {} anos'.format(media))
print ('O homem mais velho se chama {} e tem {} anos!'.format(nomev, idadev))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totM))
