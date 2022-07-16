from random import randint
cont = soma = v = 0
print ('-='*15)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print ('-='*15)
while True:
    num = int(input('Digite um número: '))
    IP = str(input('Par ou impar [P/I]: ')).strip().upper()[0]
    print ('-'*30)
    comp = randint(1,10)
    soma = num + comp
    cont += 1
    print(f'Você jogou {num} e o computador {comp}, Total de {soma}. ', end='')
    if IP == 'I':
        if  soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif IP == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else: 
            print ('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print ('-='*15)
print (f'\033[1;31mGAME OVER.\033[m Você venceu {v} vezes.')

