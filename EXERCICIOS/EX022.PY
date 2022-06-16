
from posixpath import split


nome = str (input("Digite o seu nome completo: ")).strip()
print ("Nome em letras minúsculo:", nome.lower())
print ("Nome em maiúsluas",nome.upper())
print("O seu nome possui {} letras".format(len(nome) - nome.count(' ')))
print ("Seu primeiro nome tem {} letras".format(nome.find(' ')))
separa = nome.split ()
print ("Seu primeiro nome é {} e ele tem {} letra".format(separa[0], len (separa[0])))
