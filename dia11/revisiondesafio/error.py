class Error(Exception):
    """Clase base de Exception """
    pass

class DimensionError(Error):
    
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            retorno = self.mensaje

            if self.dimension:
                retorno+=f"\nLa dimension ingresada es {self.dimension}"

            if self.maximo:
                retorno+=f" y el maximo permitido es {self.maximo}"

            return retorno