menor = 0
maior = 0
for c in range(0,6):
    int(input(f'DIgite um valor para a posição {c}: '))
    if c >= maior:
        maior = c
    if c <= menor:
        menor = c
print(f'Você digitou os valores {c}')
print (maior)