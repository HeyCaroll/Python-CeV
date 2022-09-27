def fatorial(num, show=False):
    """_
    -> Calcular o fatorial de um número
        num > (int) Número a ser calculado
        show > (bool)Mostrar o calculo, o não
        Returns > O valor de fatorail de um número 
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat
    
   
#Programa principal 
print(fatorial(5, show=True))