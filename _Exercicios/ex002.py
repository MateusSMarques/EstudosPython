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

