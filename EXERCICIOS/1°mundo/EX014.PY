c = float(input("Informe a temperatura em °C:" ))
#f = ((9 * c) / 5) + 32
#neste caso o uso ou a ausencia de parenteses não afetara o codigo devido a ordem de precedencia
f = 9 * c / 5 + 32
print ("A temperatura de{}°C corresponde a {}°F ".format(c,f))