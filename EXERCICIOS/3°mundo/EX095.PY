dados = dict()
partidas = list ()
time = list()
while True:
    dados.clear()
    dados ['nome'] = str(input('Digite o nome: '))
    totalp = int(input('Partidas jogadas: '))
    time.clear()
    for c in range(0, totalp):
        partidas.append(int(input(f'   -Gols na {c+1} partida: ')))
    dados ['gols'] = partidas[:]
    dados ['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        res = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if res in 'NS':
            break
        print('ERRO! Responda somente com S ou N.')
    if res == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k,v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar):'))
    if resp == 999:
        break
    if resp >=len(time):
        print(f'ERRO! Não existe jogador com código {resp}')
    else:
        print(f'-- levantamento do jogador {time[resp] ["nome"]}')
        for i,g in enumerate(time[resp]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*30)
    print()
