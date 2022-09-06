def area():
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {a*b:.2f}m²')


print('-='*10)
print('CONTROLE DE TERRENOS')
print('-='*10)
a = int(input('Largura (m): '))
b = int(input('Comprimento (m): '))
area()
