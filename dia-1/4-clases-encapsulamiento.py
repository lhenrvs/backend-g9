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
        # antes de agregar la venta validar si aun tenemos stock para dicha venta
        # primero ver si tenemos ventas, si hay iteramos esas ventas y sacamos cuanto de cantidad hemos vendido. Luego ver si ese numero es menor que la 
        # cantidad total(el atributo cantidad) si es mayor indicar que ya hemos sobregirado las ventas. por ultimo a esa cantidad de productos vendidos 
        # sumar la cantidad entrante y ver si es menor o igual que la cantidad total, si lo es, entonces generar la venta, caso contratio, no permiti la venta e indicar que no hay stock suficiente
        # indicar cuanto es lo que tenemos para vender
        venta = {
            'fecha' : fecha,
            'cliente' : cliente,
            'cantidad' : cantidad
        }
        self.__ventas.append(venta)
        print(self.__sacar_igv(self.precio))
        print('venta registrada exitosamente')
    
    def mostrar_ventas(self):
        # retornar las ventas registradas de ese producto
        return self.__ventas
    
    def __sacar_igv(self, precio):
        # este metodo pasa a ser privado desde que le ponemos '__' al inicio del nombre
        return (precio * 1.18) - precio

detergente = Producto(nombre='detergente sapito', precio=4.50, cantidad=50)
detergente.nombre = 'detergente lechuga'
print(detergente.nombre) 

detergente.generar_venta(fecha='2022-10-19', cliente='eduardo de rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='julissa peres', cantidad=30)       
detergente.generar_venta(fecha='2022-10-30', cliente='franco portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='michael ordoñez', cantidad=15)

print(detergente.mostrar_ventas())

# no se puede acceder al metodo __sacar_igv   
#print(detergente.__sacar_igv(80))
