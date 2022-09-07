def area():
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {a*b:.2f}m²')

# Programa principal
print('-='*10)
print('CONTROLE DE TERRENOS')
print('-='*10)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area()
