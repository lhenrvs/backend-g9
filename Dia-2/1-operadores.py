# Operadores artimeticos
numero1, numero2 = 10, 50

# suma
# Nota: solamente sera suma si las dos variables son numericas, si es que son string 
# entonces se hara una concatenación y ademas no se puede sumar entre string y numeros
print(numero1 + numero2)

# resta
print(numero1 - numero2)
# print('ab' - 'bc')

#multiplicacion
#nota: si se usa la multiplicacion en un string con un numero, entonces el string se repetira la cantidad de
#veces que tenga el valor del numero.
print(numero1 * numero2)
print('hola' * 5)

#division
print(numero1/numero2)

#Modulo
print(numero1 % numero2)

# Cociente
print(numero1 // numero2)

#exponente
#10^50
print(numero1 ** numero2)

#-----------------------------------------------
#OPERADORES ASIGNACION
# igual asignar un nuevo valor a una varialbe
numero1 = 100

#incremento
numero1 += 1 # incrementando el valor de numero1 en una unidad.
print(numero1)

# decremento (las dos formas son iguales)
numero1 -= 1
numero1 = numero1 - 1
print(numero1)

# multiplicador
numero1 *= 2  # aumento multiplicando *2
print(numero1)

# DIVIDENDO
numero1 /= 5 # numero1 = numero1/5
print(numero1)

#-----------------------------------------------------
#  OPERADORES DE COMPRACIONES (siempre retornaran un booleano (si es verdadero o si es falso))
# igual que
# nota: en python, a diferencia de java script, no existe el tiple igual (comparador de tipos de datos)
print(numero1 == numero2)
print(type(numero1)== type(numero2))

# MAYOR | MAYOR QUE
print(10>9.58)
print(10 > int('5'))
print(50 >= 30)

