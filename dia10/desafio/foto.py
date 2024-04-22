""" 
Carlos Urrutia
Jimena Traipe
Flavia Cayún
Yessenia Millar
Matías Valdivia
Diego Larenas
"""

from error import DimensionError

class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str):
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta  # Asignación correcta del atributo ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int):
        try:
            if 0 < ancho < self.MAX: 
                self.__ancho = ancho
            elif ancho < 1:  # Error por dato menor a 1
                raise DimensionError("El valor del ancho debe ser mayor que 0.", ancho, self.MAX)
            elif ancho > self.MAX:  # Error por dato mayor que el máximo
                raise DimensionError("El valor del ancho excede el máximo.", ancho, self.MAX)
        except DimensionError as dError:
            print(dError)
        except TypeError:
            print("Error en el ingreso del ancho")
        else:
            print("Ancho editado")

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto):
        try:
            if 0 < alto < self.MAX:
                self.__alto = alto
            elif alto < 1:
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
    foto.ancho = 0  # El valor del ancho debe ser mayor que 0. La dimensión ingresada es: 0 y el máximo es: 2500.
    foto.ancho = 3000  # El valor del ancho excede el máximo. La dimensión ingresada es: 3000 y el máximo es: 2500.
    foto.alto = 0  # El valor del alto debe ser mayor que 0. La dimensión ingresada es: 0 y el máximo es: 2500.
    foto.alto = 3000  # El valor del alto excede el máximo. La dimensión ingresada es: 3000 y el máximo es: 2500.
    foto.alto = "a"  # Error en el ingreso del alto
    foto.ancho = 2480  # Ancho editado
    foto.alto = 2495  # Alto editado