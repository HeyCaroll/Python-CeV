valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i}: ')))

print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for i in range(0, 5):
    if valores[i] == max(valores):
        print(i, end=' ')
print()
print(f'O maior valor digitado foi {min(valores)} na posição ', end='')
for i in range(0, 5):
    if valores[i] == min(valores):
        print(i, end=' ')
