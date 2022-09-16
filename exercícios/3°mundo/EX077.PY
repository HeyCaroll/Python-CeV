palavras = ('livros', 'cafe', 'gatos', 'musica', 'programaçao', 'python', 'aprender')
print('='*40)
print(f'{"CONTANDO VOGAIS":^35}')
print('='*40)
for p in palavras:
    print(f'\nNa palavras {p.upper()} temos: ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra,end=' ')

