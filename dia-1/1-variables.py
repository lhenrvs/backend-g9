edad = 10
nombre = 'luis'
print(nombre)

# en python no hay ni null ni undefined ni nan (not a number) todo ello se resumen en None
especialidad = None
# la variable especialidad con el None, quiere decir que esta vacia esa variable
#type(var) > devolver que tipo de dato es esa variable
print(type(nombre))

# se puede declarar varias variables en una misma linea
curso, grupo, mes = 'codigo', 'backend', 'octubre'
print(grupo)

#el id, es para decir la posicion de la memoria en donde esta almacenada la variable, 
# esa posicion cambia conforme se corre el programa.
print(id(curso))