x = float (input("Qual é o salário do funcionario? R$"))

novo = x + (x * 15 / 100)

print ("Um funcionario que recebia R${:.2f} e ganha 15% de aumento passara a receber {:.2f}".format(x, novo))