n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
num = (n1,n2,n3,n4)
print(f'Você digitou os valores {num}.')
if 9 in num:
    print (f'O número 9 apareceu {num.count(9)} vezes.')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print (f'O número 3 apareceu na {num.index(3)+1}° posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares são: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


