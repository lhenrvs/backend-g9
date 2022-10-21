# herencia > sirve para reutilizar una clase previamente definida

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_resumen(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo
        }

class alumno(Usuario):

    def __init__(self, nombre, apellido, correo, telefono_emergencia):
        self.telefono_emergencia = telefono_emergencia
        super().__init__(nombre, apellido, correo)

    def saludar(self):
        print('hola yo soy la clase alumno y el nombre es {}'.format(self.nombre))

    def mostrar_resumen(self):

        resumen = super().mostrar_resumen()
        resumen['telefono_emergencia'] = self.telefono_emergencia
        return resumen
        
usuario01 = Usuario(nombre='eduardo', apellido='de rivero', correo='ederivero@gmail.com')
usuario02 = Usuario('eduardo', 'de rivero', 'ederivero@gmail.com')
usuario03 = Usuario(correo='ederivero@gmail.com', apellido='de rivero', nombre='eduardo')

print(usuario01.mostrar_resumen())

alumno01 = alumno('juan', 'martinez', 'jmartinez@yahoo.es', '947852190')
alumno01.saludar()
print(alumno01.mostrar_resumen())
