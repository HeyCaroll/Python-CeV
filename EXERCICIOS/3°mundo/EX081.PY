num = []
count = 0
while True: 
    num.append(int(input('digite um número: ')))
    count += 1
    perg = str(input('Deseja continuar? [S/N] '))
    if perg in 'Nn':
        break
print (f'Você digitou {count} números')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print ('o número 5 está na lista !')
else:
    print('O número 5 não está na lista !')