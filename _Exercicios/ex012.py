import random
n1 = input('Escolhe um nome: ')
n2 = input('Escolhe um nome: ')
n3 = input('Escolhe um nome: ')
n4 = input('Escolhe um nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print (' o escolhido foi: {}'.format(escolhido))
