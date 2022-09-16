from turtle import distance


dist = float(input("Qual é a distancia da viagem?  "))
print ("Você está prestes a começar uma viagem de  {}km".format(dist))

if dist <= 200:
    preço = dist * 0.50
    print("O preço de sua passagem será R${:.2f}".format(preço))
else:
    preço = dist * 0.45
    print ("O preço da sua passagem será de R${:.2f}".format(preço))