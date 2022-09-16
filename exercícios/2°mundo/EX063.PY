print ('-'*40)
print ('    Sequência de Fibonacci')
print('-'*40)
termo = int(input('Quantos termos você deseja mostrar? '))
n1 = 0
n2 = 1
cont = 3
print('{} - {}'.format(n1, n2), end='')
while cont <= termo:
    n3 = n1 + n2
    print (' - {}'.format(n3), end='')
    n1 = n2 
    n2 = n3
    cont += 1
print ('- FIM')
print ('~'*40)
