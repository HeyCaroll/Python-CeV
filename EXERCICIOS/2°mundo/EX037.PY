n = int(input('Digite um número inteiro: '))
print('=-='*20)
print ('''escolha um das bases para conversão: 
[ 1 ] conversão para BINARIO
[ 2 ] conversão para OCTAL 
[ 3 ] conversão para HEXADECIMAL''')
print('=-='*20)

x = int(input('Sua opção: '))

if x == 1:
    print ('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif x == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif x == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31mERRO!\033[m alguma coisa está errada...')
    
