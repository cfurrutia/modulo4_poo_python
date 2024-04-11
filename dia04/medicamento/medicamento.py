class Medicamento():
    IVA = 0.18  # Tasa de impuesto al valor agregado

    # constructor de la clase que inicializa los atributos de nombre y stock
    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre  # nombre del medicamento
        self.stock = stock  # número de unidades en stock
        self.precio_bruto = 0  # precio original del medicamento
        self.precio_final = 0.0  # precio final del medicamento, incluyendo IVA y descuentos
        self.descuento = 0.0  # porcentaje de descuento aplicado al precio final


    @staticmethod
    #se utiliza para validar que el precio bruto sea mayor a cero antes de calcular el IVA y los descuentos.
    def validar_mayor_a_cero(numero: int):
        """
        Valida si un número es mayor que cero
        """
        return numero > 0
    
    @property
    # propiedad que obtiene el precio final del medicamento, incluyendo el IVA y los descuentos
    def precio(self):
        """
        Obtiene el precio final del medicamento
        """
        return self.precio_final
    
    @precio.setter
    def precio(self, precio_bruto: int):
        """
        Establece el precio final del medicamento, aplicando el impuesto IVA y descuentos si es necesario
        """
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA

            if self.precio_final >= 10000 and self.precio_final < 20000:
                self.descuento = 0.1
            elif self.precio_final >= 20000:
                self.descuento = 0.2

            if self.descuento:
                self.precio_final *= 1 - self.descuento

    # método especial que compara dos instancias de la clase por su nombre (ignorando mayúsculas y minúsculas)
    def __eq__(self, other):
        """
        Compara dos instancias de la clase por su nombre (ignorando mayúsculas y minúsculas)
        """
        return self.nombre.lower() == other.nombre.lower()
    
    # método especial que agrega el stock de dos instancias de la clase si tienen el mismo nombre
    def __iadd__(self, other):
        """
        Añade el stock de dos instancias de la clase si tienen el mismo nombre
        """
        if self == other:
            self.stock += other.stock
        return self
    
    # método especial que devuelve una representación en forma de cadena de los atributos de la instancia
    def __str__(self):
        """
        Devuelve una representación en forma de cadena de las variables de la instancia
        """
        return f""" nombre:{self.nombre}
        stock: {self.stock}
        precio bruto: {self.precio_bruto}
        precio final: {self.precio_final}
        descuento: {self.descuento}"""
