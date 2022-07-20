n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
    'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        break
    else:
        print('Tente Novamente. ', end='')
print (f'Você digitou o número {n[num]}')