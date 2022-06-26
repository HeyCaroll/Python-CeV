import time
print ('-=-'*20)
print('''\033[1;94mEQUILÁTERO:\033[mtodos os lados iguais
\033[1;94mISÓSCELES:\033[m dois lados iguais
\033[1;94mESCALENO:\033[m todos lados diferentes''')
print ('-=-'*20)
time.sleep(5)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2+n3 and n2 < n3+n1 and n3 < n1+n2:
    print('Os segmentos \033[1;92mpodem\033[m formar um triangulo ', end='')
    if n1 == n2 == n3:
        print ('\033[1;37mequilátero!\033m')
    elif n1 != n2 != n3 != n1:
        print('\033[1;37mescaleno!\033m')
    else:
        print('\033[1;37misósceles\033m')
else:
    print('Os segmentos \033[1;31mnão podem\033[m formar um trinangulo!')