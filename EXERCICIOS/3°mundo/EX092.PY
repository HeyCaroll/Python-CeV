from datetime import datetime
dados = dict()
dados ['nome'] = str(input('Digite o seu nome: '))
nas = int(input('Ano de nascimento: '))
dados ['idade'] = datetime.now().year - nas
dados ['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))
if dados['ctps'] != 0:
    dados ['contra'] = int(input('Ano de contratação: '))
    dados ['salarios'] = float(input('Salário: R$'))
    dados ['aposentadoria'] = dados['idade'] +((dados['contra'] + 30) - datetime.now().year)
print('=-'*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')
