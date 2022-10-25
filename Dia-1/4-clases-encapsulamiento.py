# encapsulamiento > ES EL METODO DE 'OCULTAR cierta  información sencible o que no debe ser manipulada desde fuera de la clase (atributo o metodo privado)
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        # __atributo > estaremos indicando que no sera privado y por ende no puede ser accedido desde fuera de la clase PRIVADO
        self.__ventas =[]
        # _atributo > ATRIBUTO PROTEGIDO en python mas que todo funciona para cuando queremos utilizar este atributo con herencia 
        self._precio_mayorista = 100

    def generar_venta(self, fecha, cliente, cantidad):
        venta = {
            'fecha' : fecha,
            'cliente' : cliente,
            'cantidad' : cantidad
        }
        self.__ventas.append(venta)

        print('venta registrada exitosamente')
    
    def mostrar_ventas(self):
        # retornar las ventas registradas de ese producto
        return self.__ventas

detergente = Producto(nombre='detergente sapito', precio=4.50, cantidad=50)
detergente.nombre = 'detergente lechuga'
print(detergente.nombre) 

detergente.generar_venta(fecha='2022-10-19', cliente='eduardo de rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='julissa peres', cantidad=30)       
detergente.generar_venta(fecha='2022-10-30', cliente='franco portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='michael ordoñez', cantidad=15)

print(detergente.mostrar_ventas())