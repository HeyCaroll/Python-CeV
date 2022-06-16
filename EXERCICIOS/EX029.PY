v = int(input("Qual é a velocidade atual do carro ? "))
if v <= 80:
    print("Está dentro do permetido, tenha uma boa viagem!")
else:   
    multa = (v - 80) * 7
    print ("MULTADO! Você ultrapassou do limite permitido que é 80Km/h")
    print ("Você devera pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! Digira com segurança.")