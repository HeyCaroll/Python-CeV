from this import d


x = float(input("Qual é o preço do produto? R$ "))
d = x - (x * 5 / 100)
print("Aplicando o desconto de 5%, o valor passa a ser R${}".format(d))