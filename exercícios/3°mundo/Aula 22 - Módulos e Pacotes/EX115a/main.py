from lib.interface import *

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if res == 1:
        cabeçalho('Pessoas cadastradas')
    if res == 2:
        cabeçalho('Cadrastrar nova pessoa')
    if res == 3:
        cabeçalho('Saindo do sistema. Até logo!')
        break
