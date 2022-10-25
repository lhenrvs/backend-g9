# el try va de la mano con el except, no pueden ir separados
try:
    #print(10/0)

    int('a')
except ZeroDivisionError:
    #aca ingresara si el error es de tipo zerodivision    
    print('hubo un error al dividir entre 0')
except ValueError: 
    # aca entrara si hubo un error de conversion a entero
    print('error al convertir el numero')   
except Exception as error:
    #aca entrara si el error es otro generico
    # .args > es el artibuto de toda instancia de exception que me devolvera el porque se dio ese error(argumentos)
    print(error.args)

try:
    # args son los argumentos que nosotros indicaremos o que recibimos cuando se da un error, en este atributo se podran obtener todos los argumentos del porque se dio ese error
    raise Exception('eres menor de edad', 'no eres peruano', 'no eres femenino') 
except Exception as error:
    print(error.args)       
    
try:
    resultado = 5/1
    raise Exception('error desconocido')
    
except Exception as error:
    print(error.args)

else:
    # en el caso que el codigo se ejecutase sin ningun error ( sin ingresar al except)
    print('la operacion se realizo exitosamente')

finally:
    #ingresa si la ejecucion estuvo bien o si ingreso al except
    print('si la operacion estuvo bien o mal igual se ejecuta')

#ejercicios:
#recibir por el teclado un numero

try:
    numero = input('ingresa un numero: ')
    int(numero)
#luego convertir a ese numero a un entero(si no se puede indicar que el valor es incorrecto). sumar 10 mas ese numero ingresado y devolver
except ValueError:
    print('error al convertir el numero')
else:
    final = numero + 10
    print(final)