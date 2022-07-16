while True:
    t = int(input('Deseja ver a tabuada de qual número ? '))
    if t < 0:
        break
    print('---'*15)
    for c in range(1,11):
        print (f'{t} x {c} = {t*c}')
    print('---'*15)
print ('Programa tabuada encerrado. Volte sempre! ')