# programa.py
from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

# Función que crea una tienda con nombre,costo de delivery y tipo de tienda 
def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = int(input("Ingrese el costo de delivery: "))
    tipo_tienda = int(input("Ingrese el tipo de tienda (1. Restaurante, 2. Supermercado, 3. Farmacia): "))
    if tipo_tienda == 1:
        return Restaurante(nombre, costo_delivery)
    elif tipo_tienda == 2:
        return Supermercado(nombre, costo_delivery)
    elif tipo_tienda == 3:
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None
    
# Función que permite ingresar productos a la tienda
def ingresar_productos(tienda):
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock_entrada = input("Ingrese el stock del producto (deje vacío para asumir 0): ")
        stock = int(stock_entrada) if stock_entrada else 0 # inicializa con 0 siempre
        producto = Producto(nombre, precio, stock)
        tienda.ingresar_producto(producto)
        ingresar_otro = input("¿Desea ingresar otro producto? (si/no): ")
        if ingresar_otro.lower() != "si":
            break
        
# Función principal que crea una tienda, permite ingresar productos y realizar ventas
def main():
    tienda = crear_tienda()
    if tienda:
        ingresar_productos(tienda)
        while True:
            accion = int(input("¿Qué desea hacer? (1. listar productos, 2. realizar venta, 3. salir): "))
            if accion == 1:
                print(tienda.listar_productos())
            elif accion == 2:
                nombre_producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad a vender: "))
                print(tienda.realizar_venta(nombre_producto, cantidad))
            elif accion == 3:
                break

# llamar a la función
if __name__ == "__main__":
    main()