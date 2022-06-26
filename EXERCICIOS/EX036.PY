casa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qualo valor do seu salário: "))
parcela = int(input("Em quantos anos deseja parcelar? "))

x = casa / (parcela * 12)
min = salario * 30 / 100

print ("O valor mensal da casa será de R${:.2f} por mês, em {} anos".format(x, parcela))

if x <= min:
    print("Seu emprestimo foi \033[1;31mNEGADO!\033[1;31m")
else:
    print("Seu emprestimo foi \033[0;32mACEITO!\033[0;32m")
