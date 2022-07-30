lista = [] 
par = []
imp = []
while True:
    lista.append(int(input('Digite um número: ')))
    res = (str(input('Deseja continuar? [S/N] '))).strip().upper()
    if res in "N":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print('---'*10)
print(f'A lista completa é {lista}')
print (f'A lista de pares é {par}')
print(f'A lista de ímpares é {imp}')
