def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO!\033[m "{entrada}" é um preço inválido!')
        else:
            valido = True
            return float(entrada)