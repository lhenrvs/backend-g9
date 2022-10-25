class Documento:
    def __init__(self, tipo, num_paginas, editable, contenido):
        # __init__ > sera el metodo que se llame cuando cremos una instancia de la clase
        # en el constructor definimos un nuevo atributo entonces este se creara para toda la clase
        self.tipo = tipo
        self.num_paginas = num_paginas
        self.editable = editable
        self.contenido = contenido
    
    def editar_documento(self, nuevo_contenido):
        # si el documento no es editable entonces indicar que no se puede editar el documento, caso contratio modificar la información del atributo contenido
        if(self.editable==False):
            print('el archivo no puede ser modificado')
        else:
            self.contenido = nuevo_contenido
            print('el archivo fue modificado')

mi_curriculum = Documento(tipo='PDF', num_paginas=80, editable=False, contenido='soy developer')

proforma_pagina_web = Documento(tipo='WORD', num_paginas=3, editable=True, contenido='la pagina web vale 2500 soles')

mi_curriculum.editar_documento(nuevo_contenido='ahora soy diseñador')

proforma_pagina_web.editar_documento(nuevo_contenido='la pagina vale 4000 soles')
