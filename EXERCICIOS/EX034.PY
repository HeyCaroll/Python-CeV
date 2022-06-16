x = float(input("Qual o salario do funcionario ? R$"))
if x <= 1250:
    y = x + (x * 15 / 100)
else:
    y = x + (x * 10 / 100)
print("O funcionario que recebia {:.2f}, passará a receber {:.2f}".format(x, y))
