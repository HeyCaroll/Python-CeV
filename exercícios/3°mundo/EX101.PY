def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'-> O eleitor possui {idade} anos, logo o seu voto é ',end='')
    if idade >= 18 :
        return '\033[1;32mobrigatorio\033[0;0m'
    elif idade >=16 or idade >= 65:
        return '\033[1;33mopcional\033[0;0m'
    elif idade < 16:
        return '\033[1;31mnegado\033[0;0m'


#Programa principal
ano = int(input('em que ano você nasceu? '))
print(voto(ano))
