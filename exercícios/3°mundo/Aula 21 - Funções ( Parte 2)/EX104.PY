def leiaInt(msg):
    certo = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            certo = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if certo:
            return valor
            
        

#Programa principal
n = leiaInt ('Digite um número: ')
print(f'Você acabou de digitar o número {n}')