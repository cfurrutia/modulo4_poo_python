""" 
Carlos Urrutia
Jimena Traipe
Flavia Cayún
Yessenia Millar
Matías Valdivia
Diego Larenas
"""

from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str):
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int: #getter
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho:int): #setter con control de errores
        try:
            if ancho > 0 and ancho < self.MAX: #caso sin error
                self.__ancho = ancho #setter funciona
            elif ancho < 1: #error por dato menor a 1
                raise DimensionError("El valor del ancho debe ser mayor que 0.", ancho, self.MAX)
            elif ancho > self.MAX: #error por dato mayor que el máximo
                raise DimensionError("El valor del ancho excede el máximo.", ancho, self.MAX)
        except DimensionError as dError: #impresión del error en caso de un Dimension Error
            print(dError)
        except TypeError: #En caso de errores de tipo
            print("Error en el ingreso del ancho")
        else:
            print("Ancho editado") #si no hay errores, que reporte el cambio realizado

        

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto > 0 and alto < self.MAX:
                self.__alto = alto
            elif alto < 1 :
                raise DimensionError("El valor del alto debe ser mayor que 0.", alto, self.MAX)
            elif alto > self.MAX:
                raise DimensionError("El valor del alto excede el máximo.", alto, self.MAX)
        except DimensionError as dError:
            print(dError)
        except TypeError:
            print("Error en el ingreso del alto")
        else:
            print("Alto editado")


if __name__ == "__main__":
    foto = Foto(1500, 2100, "blabla")
    foto.ancho = 0 #El valor del ancho debe ser mayor que 0. La dimensión ingresada es: 0 y el máximo es: 2500.
    foto.ancho = 3000 #El valor del ancho excede el máximo. La dimensión ingresada es: 3000 y el máximo es: 2500.
    foto.alto = 0 #El valor del alto debe ser mayor que 0. La dimensión ingresada es: 0 y el máximo es: 2500.
    foto.alto = 3000 #El valor del alto excede el máximo. La dimensión ingresada es: 3000 y el máximo es: 2500.
    foto.alto = "a" #Error en el ingreso del alto
    foto.ancho = 2480 #Ancho editado
    foto.alto = 2495 #Alto editado