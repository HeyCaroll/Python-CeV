x = int(input("Primeiro número: "))
y = int(input("Segundo número: "))
z = int(input("Terceiro número: "))
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z

maior = x
if z > y and z > x:
    maior = z
if z > x and z > y:
    maior = z
print ("O menor número é {}".format(menor))
print ("O maior número é {}".format(maior))