from ast import arg
from inspect import ArgSpec


def sumar(num1, num2, num3):
    return num1 + num2 + num3

def sumar_n_numeros(*args):
    # args > arguments sera recibir N (ilimitado) numero de parametros
    print(args)
    # sumar todos los valores de la tupla args utilizando un for
    suma = 0
    for numero in args:
        print(numero)
        suma = suma + numero
    suma2 = 0
    for posicion in range(0, len(args)):
        print(posicion)
        suma2 = suma2 + args[posicion]

    print(suma2)
    return suma

print(sumar(5, 10, 7))

resultado = sumar_n_numeros(10, 5, 18, 7, 22, 56, 89)

print(resultado)




