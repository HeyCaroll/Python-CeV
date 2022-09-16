from random import randint
palpite = 0
acertou = False
pc = randint(0,10)
print ('Olá, sou o seu computador, e acabei de pensar um número entre 0 e 10.')
print ('Será que você consegue adivinhar qual foi? ')
while not acertou:
    p = int(input('Qual é o seu palpite? '))
    palpite += 1
    if p == pc:
        acertou = True
    else:
        if p < pc:
            print('Mais... Tente mais uma vez.')
        elif p > pc:
            print('Menos... Tente mais uma vez.')
print ('Acertou com {} tentativas. Parabéns!'.format(palpite))
