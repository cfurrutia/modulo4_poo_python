from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1:
                raise DimensionError("Ancho no debe ser menor que 1",ancho)
            elif ancho > self.MAX:
                raise DimensionError(f"Ancho no debe ser mayor a {self.MAX}",ancho,self.MAX)
            else:
                self.__ancho = ancho
        except DimensionError as de:
                    print("Error::",de)#llamado al str

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto < 1:
                raise DimensionError("Alto no debe ser menor que 1",alto)
            elif alto > self.MAX:
                raise DimensionError(f"Alto no permitido",alto,self.MAX)
            else:
                self.__alto = alto
        except DimensionError as de:
            print("Error::",de)#llamado al str

if __name__ == "__main__":
    foto = Foto(2500,2500,"ruta")

    #modificacion
    foto.alto = 2600