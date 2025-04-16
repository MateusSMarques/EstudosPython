import random
n1 = input('Escolhe um nome: ')
n2 = input('Escolhe um nome: ')
n3 = input('Escolhe um nome: ')
n4 = input('Escolhe um nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print ('A ordem ficou: ')
print(lista)
