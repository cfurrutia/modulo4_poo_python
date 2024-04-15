# producto.py
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = max(value, 0)   # Establece el stock del producto, asegurándose de que no sea negativo

    def __add__(self, other):
        if self.__nombre == other.nombre:
            self.stock += other.stock
            return self

    def __sub__(self, other):
        if self.__nombre == other.nombre:
            self.stock -= other.stock
            return self

    def __eq__(self, other):
        return self.__nombre == other.nombre

    def __str__(self):

        return f"{self.nombre}: ${self.precio}{' (Stock: ' + str(self.stock) + ')' if self.stock else ''}"