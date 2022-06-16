from math import hypot
co = float (input("Comprimento do cateto oposto: "))
ca = float (input("comprimento do cateto adjacente: "))
h = hypot (co,ca )
print ("A hipotenusa será {:.2f}".format(h))

#mesmo codigo, porém sem a importação da biblioteca math

'''co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = (co ** 2 + ca **2) ** (1/2)
print ("A hipotenusa será {:.2f}".format(h))'''

