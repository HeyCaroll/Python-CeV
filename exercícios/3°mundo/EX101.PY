from datetime import date

def voto(ano):
    nasc = int(input('Ano de nascimento: '))
    idade = date.today().year -nasc


print(idade)