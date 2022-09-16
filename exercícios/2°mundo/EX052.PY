cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;34m', end=' ')
        cont += 1
    else:
        print('\033[1;90m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m O número {} foi dividido {} vezes.'.format(num, cont))

if cont <= 2:
    print('E por isso ele \033[1;92mÉ PRIMO!\033[m'.format(num))
else:
    print('E por isso ele \033[1;91mNÃO É PRIMO!\033[m'.format(num))

