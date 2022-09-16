lista = ('Notebook', 800,
          'Mouse', 50, 
          'Fone', 70,
          'Livro', 45,
          'Café', 15)
print('='*40)
print(f'\033[1;36m{"LISTA DE VALORES":^40}\033[m')
print('='*40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}',end='')
    else:
        print(f'{lista[item]:.>6.2f}')
print('-'*40)