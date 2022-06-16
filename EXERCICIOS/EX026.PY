frase = str(input("Digite uma frase: ")).strip().upper()
print ("A letra A aprece {}".format(frase.count("A")))
print ("A primeira letra A apa {}".format(frase.find("A")+1))
print("A letra A aparece pela ultima vez em {}".format(frase.rfind("A")+1))