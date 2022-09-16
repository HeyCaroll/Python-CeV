dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-='*20)
for k,v in dados.items():
    print(f' - {k} é igual a {v}')