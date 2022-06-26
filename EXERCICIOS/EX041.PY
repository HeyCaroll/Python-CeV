import datetime
hoje = int(datetime.datetime.now().year)
ano = int (input('Ano de nascimento: '))
idade = hoje - ano 
print ('O atleta possui {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÉNIOR')
else:
    print('Classificação: MASTER') 
