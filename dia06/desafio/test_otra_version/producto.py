class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre}: ${self.precio}{' (Stock: ' + str(self.stock) + ')' if self.stock else ''}"
