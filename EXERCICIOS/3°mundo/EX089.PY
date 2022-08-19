cadrastro = list()
res = c = opc = 0
while res != 'N':
    nome = str(input('Digite o nome do aluno(a): '))
    n1 = float(input('1° Nota: '))
    n2 = float (input('2° Nota: '))
    media = ( n1 + n2 ) / 2
    cadrastro.append ([nome, [n1,n2], media])
    res = str(input('Deseja continuar ? [S/N] ')).strip().upper()
print('-='*20)
print (f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
for i,a in enumerate(cadrastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-='*20)
while opc != 999:
    opc = int (input('Mostrar a nota de qual aluno(a) <999 interrompe> :'))
    if opc <= len(cadrastro) - 1:
        print (f'Notas de {cadrastro[opc][0]} são {cadrastro[opc][1]}')
print('-='*20)
print ('Obrigado por usar nosso programa, volte sempre ;)')

