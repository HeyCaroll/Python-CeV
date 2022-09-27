from time import sleep

def maior(* num):
    cont = maior = 0
    print('=-'*20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor},', end=' ')
        sleep(0.5)
        if valor > maior:
            maior = valor
            cont += 1
    print('')
    print(f'-> Foram informado {cont} valores ao todo.')
    print(f'-> O maior número analisado foi {maior}.')
    sleep (4)


#Programa principal
maior(1, 2, 3)
maior (1, 5, 7, 11, 74, 1, 0, 2)
