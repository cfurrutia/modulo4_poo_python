class DimensionError(Exception):
    def __init__(self, mensaje:str, dimension=None, maximo=None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self): #sobrecarga del método __str__ para generar mensajes de error
        if self.dimension is not None and self.maximo is not None: #error cuando están todos los datos.
            return f"{self.mensaje} La dimensión ingresada es: {self.dimension} y el máximo es: {self.maximo}."
        else:
            return super().__str__() #en caso de que no se cumplan esas condiciones y se llame al error, llamado al método padre con super, 
        #solo retorna el "mensaje"
            
    
if __name__ == "__main__":
    foto1 = DimensionError("ERROR Dimensión Inválida") #ERROR Dimensión Inválida
    foto2 = DimensionError("ERROR Dimensión Inválida",2800, 2500) #ERROR Dimensión Inválida La dimensión ingresada es: 2800 y el máximo es: 2500.
    foto3 = DimensionError("ERROR Dimensión Inválida",-50,2500) #ERROR Dimensión Inválida La dimensión ingresada es: -50 y el máximo es: 2500.
    print(foto1)
    print(foto2)
    print(foto3)