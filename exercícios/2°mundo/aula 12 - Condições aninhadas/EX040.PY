from time import sleep
n1 = float(input("Sua primeira nota: "))
n2 = float(input("Sua segunda nota: "))
n3 = float(input("Sua terceira nota: "))
nota = (n1 + n2 + n3) / 3

print ("Sua média foi {:.2f}.".format(nota))

if nota < 5.0:
    print("Você está...")
    sleep(3)
    print ("\033[1;31mREPROVADO!\033[1;31m")
elif 6.9 > nota > 5.0:
    print("Você está...")
    sleep(3)
    print("\033[1;33mRECUPERAÇÃO!\033[1;33m")

elif nota >= 7.0:
    print("Você está...")
    sleep(3)
    print("\033[0;32mAPROVADO!\033[0;32m")