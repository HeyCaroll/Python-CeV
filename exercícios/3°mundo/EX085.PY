n = [[],[]]
v = 0
for c in range (1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print (f'Os números pares digitados foram {sorted(n[0])}')
print (f'Os números impares digitados foram {sorted(n[1])}')
