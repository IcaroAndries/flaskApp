from distutils.log import error


teste = {
    "azul" : 1,
    "preto" : 2,
    3 : 3
}

try:
    c = teste[3]
except KeyError:
    print('Não existe essa chave')
else:
    print(c)