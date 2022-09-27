x = float(input("Quantos reais você possui? R$ "))
dolar = x / 3.27
print ("Com R${:.2f}, você pode comprar US${:.2f}".format(x, dolar))