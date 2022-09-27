print ("-=" * 20)
print ("Analisando triangulos")
print ("-=" * 20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro semgmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print("Os segmentos acima formam um trinânulo!")
else:
    print ("Os segmentos não formam um triangulo!")