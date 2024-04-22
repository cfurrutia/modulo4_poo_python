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
    def ancho(self) -> int:
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho:int):
        try:
            if ancho > 0 and ancho < self.MAX:
                self.__ancho = ancho
            elif ancho < 1:
                raise DimensionError("El valor del ancho debe ser mayor que 0.", ancho, self.MAX)
            elif ancho > self.MAX:
                raise DimensionError("El valor del ancho excede el máximo.", ancho, self.MAX)
        except DimensionError as dError:
            print("ERROR en el ingreso del ancho: ", dError.mensaje)
        except TypeError:
            print("Error en el ingreso del ancho")
        else:
            print("Ancho editado")

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
            print("ERROR en el ingreso del alto: ", dError.mensaje)
        except TypeError:
            print("Error en el ingreso del alto")
        else:
            print("Alto editado")


if __name__ == "__main__":
    foto = Foto(1500, 2100, "ruta/imagen/foto/jpg/png")
    print(foto.ancho)
    foto.ancho = 0
    foto.alto=3000
    foto.alto = "a"
    foto.ancho = 2480
    foto.alto = 2495