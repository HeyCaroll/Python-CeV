def ficha(n='<desconhecido>', g = 0):
    print(f'O jogador {n} fez {g} gol(s)!')
    
    
#programa principal    
nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)