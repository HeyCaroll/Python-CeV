sexo = str(input('Digite o seu genero [F/M/NB]: ')).strip().upper()[0]
while sexo not in 'MmFfNBnbNb':
    sexo = str(input('Dados invalidos. Por favro, informe o seu genero: ')).strip().upper()[0]
print ('Genero {} registrado com sucesso.'.format(sexo))