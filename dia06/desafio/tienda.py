
from producto import Producto

class Tienda:
    # Inicializa una Tienda con un nombre y costo de delivery
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        # Agrega un producto a la lista de productos de la tienda o actualiza su stock si ya existe
        for p in self.__productos:
            if p == producto:
                p.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        # Devuelve una lista de productos 
        return '\n'.join([str(p) for p in self.__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        # Inicializa Restaurante con un nombre y costo del delivery
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        # Agrega un producto o actualiza su stock si ya existe
        for p in self.__productos:
            if p == producto:
                p.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        # Devuelve una lista de productos 
        resultado = ""
        for p in self.__productos:
            resultado += f"{p.nombre}: ${p.precio} \n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.__productos:
            if p.nombre == nombre_producto:
                return f"Venta realizada de {cantidad} unidades de {nombre_producto} en el Restaurante"
        return "El producto no existe en el restaurante"

class Supermercado(Tienda):
    
    def __init__(self, nombre, costo_delivery):
        # Inicializa un Supermercado con un nombre y costo de delivery
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p == producto:
                p.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        resultado = ""
        for p in self.__productos:
            resultado += f"{p.nombre}: ${p.precio} (Stock: {p.stock})"
            if p.stock < 10:
                resultado += " Pocos productos disponibles\n"
            else:
                resultado += "\n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.__productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    return f"Venta realizada de {cantidad} unidades de {nombre_producto}"
                else:
                    cantidad_vendida = p.stock
                    p.stock = 0
                    return f"Venta realizada de {cantidad_vendida} unidades de {nombre_producto} (Stock agotado)"
        return "El producto no existe en el supermercado"

class Farmacia(Tienda):
    
    def __init__(self, nombre, costo_delivery):
        # Inicializa una Farmacia con un nombre y costo de delivery
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p == producto:
                p.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        resultado = ""
        for p in self.__productos:
            resultado += f"{p.nombre}: ${p.precio}"
            if p.precio > 15000:
                resultado += " Envío gratis al solicitar este producto\n"
            else:
                resultado += "\n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.__productos:
            if p.nombre == nombre_producto:
                if cantidad <= 3:
                    if p.stock >= cantidad:
                        p.stock -= cantidad
                        return f"Venta realizada de {cantidad} unidades de {nombre_producto}"
                    else:
                        cantidad_vendida = p.stock
                        p.stock = 0
                        return f"Venta realizada de {cantidad_vendida} unidades de {nombre_producto} (Stock agotado)"
                else:
                    return "No se puede solicitar una cantidad superior a 3 por producto en cada venta"
        return "El producto no existe en la farmacia"