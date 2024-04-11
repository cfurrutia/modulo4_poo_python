class Auto():
    def __init__(self, color: str = "blanco"):
        self.__color = color

    def __str__(self):
        return f"Metodo sobre cargado {self.__color}"
    
nissan = Auto()
print(nissan) 

toyota = Auto("Negro")
print(toyota)
        