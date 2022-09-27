n = soma = cont = 0
while True:
    soma += n
    n = int(input('Digite um número [ 999 para parar ]: '))
    if n == 999:
        break
    cont += 1
print (f'Você digitou {cont} números e a soma entre eles se resulta em {soma}!')