p = float(input('Qual é o seu peso? (kg) '))
a = float(input('Qual a sua altura? (m) '))
imc = p / (a**2)
print ('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print ('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print ('Sobrepeso')
elif imc >=30 and imc <40:
    print ('Obesidade')
else:
    print('Obesidade mórbida')