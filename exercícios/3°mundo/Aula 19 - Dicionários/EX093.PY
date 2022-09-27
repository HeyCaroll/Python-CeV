dados = dict()
partidas = list ()

dados ['nome'] = str(input('Digite o nome: '))
totalp = int(input('Partidas jogadas: '))
for c in range(0, totalp):
    partidas.append(int(input(f'   -Gols na {c+1} partida: ')))
dados ['gols'] = partidas[:]
dados ['total'] = sum(partidas)
print('=-'*20)
print (dados)
print('-='*20)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i,v in enumerate(dados['gols']):
    print(f'    => Na partiad {i}, fez {v} gols.')
print (f'Foram um total de {dados["total"]} gols.')

