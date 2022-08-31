from tkinter import N


dados = dict()

dados ['nome'] = str(input('Digite o nome: '))
dados ['partidas'] = int(input('Partidas jogadas: '))
for c in range(dados['partidas']):
    dados ['gols'] = int(input(f'Gols na {c+1} partida: '))
   
print (dados)
print(f'Nome do jogador(A): {dados["nome"]}')
print (f'Quantas partidas {dados["nome"]} jogou? {dados["partidas"]}')
for k,v in range.enumerate(dados["partidas"]):
    print(f'Quantos gols na partida {k}: ')