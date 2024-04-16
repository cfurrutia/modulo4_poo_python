class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamanio: int):
        #atributos de instancia
        self.__tamanio = tamanio #atributo oculto/privado

    #metodos estaticos

    #metodos de instancia
    def cambia_color(self, color: str):
        if color != "":
            self.color = color    
    
    #sobrecarga
    def __str__(self):
        return f"El color es {self.color}, y de tamanio {self.__tamanio}"

    #getter - setters
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else:
            self.__tamanio = 0

#HERENCIA -> hereda TODO, y cada uno de los hijos puede tener sus propios metodos y atributos
class Hija(Padre):
    peso = 100

class Hijo(Padre):
    deuda = 120

class Nieto(Hija):
    pañal = "XL"

#instancia de la clase hija (creando un objeto)
hijita = Hija(100)
hijita.cambia_color("")
print(f"el color de la clase hija es {hijita.color}")

regalon = Nieto(50)