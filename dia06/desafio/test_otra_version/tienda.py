from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.nombre = nombre
        self.costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                p.stock += producto.stock
                return
        self.productos.append(producto)

    def listar_productos(self):
        return '\n'.join([str(p) for p in self.productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return f"Venta realizada de {cantidad} unidades de {nombre_producto} en el Restaurante"
                else:
                    cantidad_vendida = producto.stock
                    producto.stock = 0
                    return f"Venta realizada de {cantidad_vendida} unidades de {nombre_producto} "
        return "El producto no existe en el restaurante"

class Supermercado(Tienda):
    def listar_productos(self):
        resultado = ""
        for producto in self.productos:
            resultado += f"{producto.nombre}: ${producto.precio} (Stock: {producto.stock})"
            if producto.stock < 10:
                resultado += " Pocos productos disponibles\n"
            else:
                resultado += "\n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return f"Venta realizada de {cantidad} unidades de {nombre_producto}"
                else:
                    cantidad_vendida = producto.stock
                    producto.stock = 0
                    return f"Venta realizada de {cantidad_vendida} unidades de {nombre_producto} (Stock agotado)"
        return "El producto no existe en el supermercado"

class Farmacia(Tienda):
    def listar_productos(self):
        resultado = ""
        for producto in self.productos:
            resultado += f"{producto.nombre}: ${producto.precio}"
            if producto.precio > 15000:
                resultado += " Envío gratis al solicitar este producto\n"
            else:
                resultado += "\n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if cantidad <= 3:
                    if producto.stock >= cantidad:
                        producto.stock -= cantidad
                        return f"Venta realizada de {cantidad} unidades de {nombre_producto}"
                    else:
                        cantidad_vendida = producto.stock
                        producto.stock = 0
                        return f"Venta realizada de {cantidad_vendida} unidades de {nombre_producto} (Stock agotado)"
                else:
                    return "No se puede solicitar una cantidad superior a 3 por producto en cada venta"
        return "El producto no existe en la farmacia"
