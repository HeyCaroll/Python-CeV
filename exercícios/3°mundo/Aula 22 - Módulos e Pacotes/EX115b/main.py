from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    criarAquivo(arq)

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if res == 1:
        lerArquivo(arq)
    if res == 2:
        cabeçalho('Cadrastrar nova pessoa')
    if res == 3:
        cabeçalho('Saindo do sistema. Até logo!')
        break
