import math
a = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(a))
print ("o ângulo de {} tem o SENO de {:.2f}".format(a, seno))
cos = math.cos(math.radians(a))
print ("O ângulo de {} tem o COSENO de {:.2f}".format(a, cos))
tan = math.tan(math.radians(a))
print ("O ângulo de {} tem a TANGENTE de {:.2f}".format(a,tan))
