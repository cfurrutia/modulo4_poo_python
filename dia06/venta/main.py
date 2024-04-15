from venta import Venta, DetalleVentaItem

venta = Venta()

opcion = int(input("¿Desea ingresar un ítem a la venta?\n""1. Sí\n2. No\n"))

while opcion == 1:
    producto = input("\nIngrese nombre del producto vendido:\n")
    cantidad = int(input("\nIngrese cantidad vendida del producto:\n"))
    
    # venta.modificar_detalle(producto, cantidad)
    dti = DetalleVentaItem(producto,cantidad)
    venta.modificar_detalle(dti)
    
    opcion = int(input("\n¿Desea ingresar un ítem a la venta?\n""1. Sí\n2. No\n"))
    
print(venta.detalle)    


