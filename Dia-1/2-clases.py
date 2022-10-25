class Persona:
    estatura = 1.73
    peso = 92
    signo = 'TAURO'
    # metodos magicos: se reconocen por tener __ al inicio y al ginal del nombre del metodo
    def __str__(self):
        # el metodo __str__ sirve para indicar que cuando se mande a llamar a la clase a imprimir se modificara la impresión 
        # predeterminada que mostraba la ubicacion de memoria por lo que se va a retornar, solamente se puede retornar str
        return 'bienvenido a la clase persona'
    
    def saludar(self):
        #self > en python en todas las funciones dentro de una clase (ahora las funciones pasan a llamarse METODOS) Y para que 
        # pueda utilizar la propia configuracion de la clase (como sus atributos y otros metodos) se declara como primer parametro la palabra 'self
        texto = 'hola soy una persona y mido ' + str(self.estatura)
        print(texto)
    
    def saludar_cordialmente(self, nombre):
        texto = 'hola {}, mucho gusto. ' .format(nombre)
        return texto

# variable > instancia de la clase
eduardo = Persona()
gabriela = Persona()
eduardo.estatura = 1.89
gabriela.estatura = 1.75

# retorna el nombre de la clase en formato string
print(eduardo.__name__)
print(eduardo)
print(eduardo.estatura)
print(gabriela.estatura)

eduardo.saludar()
gabriela.saludar()
resultado = eduardo.saludar_cordialmente('angel')

print(resultado)

