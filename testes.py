print('Assim que imprime mensagem')
p = input ('escolha uma palavra: ')
print ('outro jeito de imprimir uma palavra, sua palavra é {0}'.format(p))

a = input('digite um valor: ')
print ('O tipo primitivo dele é ', type(a))  # o type mostra o tipo primitivo
# o imput sempre vai retornar o tipo como string por padrão, esmo sendo um número
print('Só tem espaços? ', a.isspace()) # ele detecta se tem apenas espaços, sem numero ou letras
print ('É um número?', a.isnumeric())
print('É alfabético? ', a.isalpha())
print ('É alfanumérico? ', a.isalnum())
print ('Está em letra maiúscula? ', a.isupper())
print ('Está em letra minúscula? ', a.islower())
print ('Está capitalizada? ', a.istitle()) #significa que tem letra maiscula e minuscula

# ** ( simbolo de potencia ) 7/2 pro simbolo de //, a resposta é o 2, que foi o numero que foi feita a divisao, aqui sendo o 3,
# a % é o resto, que nesse caso é 1
# ordem de precedencia: 1° (), 2° **, 3° *, /, //, %, 4° +, -
# para fazer raíz é **1/2

# import math, vc importou a biblioteca de matematica, vc pode usar esse import para outras bibliotecas tbm
#from math import sqrt, floor, aqui vc importa comandos especificos de uma biblioteca
import math
num = int(input('escolha um número: '))
raiz = math.sqrt(num)
print ('A raiz quadrada do {} é {:.2f}'.format(num, raiz)) #esse :.2f, significa que só vai até 3 casas decimais, pq começamos em 0, ent é 0,1,2, por isso é 3 nao dois
print ('A raiz quadrada do {} é {}'.format(num, math.floor(raiz))) #esse math.flor, eu tirei as casas decimais, deixando só o numero inteiro

import random
ran = random.randint()
print (ran)
