print ('''
\033[1;92m==============================
    10 TERMOS DE UMA PA
==============================\033[m''')
x = int(input('Primeiro termo: '))
y = int(input('Razão: '))
d = x + ( 10 - 1 ) * y
for c in range (x,d + y, y):
    print(x+c, end=' - ')
print('Fim!')