x = float(input("Largura da parede: "))
y = float(input("Altura da parede: "))

a = x * y
t = a / 2

print ("Sua parede tem a dimensão de de {} x {} e sua área é de {}m².". format(x,y,a))

print("Para pintar essa parede, você precisará de {} de tinta.".format(t))