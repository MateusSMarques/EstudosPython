import random
r = 'pedra'
s = 'tesoura'
p = 'papel'
lista = [r, s, p]
escolhido = random.choice(lista)
print (' o escolhido foi: {}, e ai ganhou ou perdeu?'.format(escolhido))
