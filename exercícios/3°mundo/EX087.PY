matriz = [[0,0,0], [0,0,0],[0,0,0]]
somap = somac = segl = 0
for l in range(0,3):
    for c in range (0,3):
        matriz[c][l] = int(input(f'Digite um número para [{l}, {c}]: '))
print ('-=-' * 20)
for l in range (0, 3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end = '')
        if matriz[l][c] % 2 == 0:
            somap += matriz [l][c]
    print ()
print ('-=-' * 20)
print (f'a soma de todos os valores pares é {somap}.')
for l in range (0,3):
    somac += matriz[1][2]
print(f'a soma de todos os valores da terceira coluna é {somac}')
for c in range (0,3):
    if c == 0 or matriz [1][c] > mai:
        mai = matriz[1][c]
print (f'O maior valor da segunda linha é {mai}')
