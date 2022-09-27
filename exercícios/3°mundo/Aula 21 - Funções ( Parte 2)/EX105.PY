def notas(*num, sit=False):
    """Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas
    :param sit: valor opcional
    :return: dicionário com várias informações sobre a situação da turma
    """
    ficha = dict()
    ficha['total'] = len(num)
    ficha['menor'] = min(num)
    ficha['maior'] = max(num)
    ficha['média'] = sum(num)/len(num)
    if sit:
        if ficha['média'] <= 8:
            ficha['situação'] = 'MB'
        if ficha['média'] <= 6:
            ficha['situação'] = 'B'
        if ficha['média'] >= 5:
            ficha['situação'] = 'I' 
    return ficha


#Programa principal
resp = notas ( 10, 2.5, 1.5, sit=True)
print(resp)
help(notas)