import math
n = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tang = math.tan(math.radians(n))
print ('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cos, tang))
