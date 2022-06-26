from random import randint
from time import sleep
comp = randint(0,5)
print ("-=-" * 20)
print ("Vou pensar em um numero entre 0 a 5, tente adivinhar...")
print ("-=-" * 20)
jogador = int(input("Adivinhe o numero que estou pensando: "))
print("PROCESSANDO...")
sleep(3)
if jogador == comp:
    print("Parabens, você adivinhou !")
else:
    print("VOCÊ PERDEU ! Eu pensei no número {}".format(comp))

