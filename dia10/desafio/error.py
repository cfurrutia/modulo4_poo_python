class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo= None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje} La dimension ingresada es: {self.dimension}, El máximo es: {self.maximo})"
        else:
            return super().__str__()
    
if __name__ == "__main__":
    foto1 = DimensionError("Error, no cumple con los rangos")
    foto2 = DimensionError("Error, no cumple con los rangos",2800, 2500)
    foto3 = DimensionError("Error, no cumple con los rangos",-50,2500)
    print(foto1)
    print(foto2)
    print(foto3)