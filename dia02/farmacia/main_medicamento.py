from medicamento import Medicamento

# paso 1
#instancia de la clase o creacion de un objeto
medicamento_nuevo = Medicamento()

# paso 2 solicitud de ingreso de datos
precio = int(input("Ingrese el precio del medicamento :"))

# paso 3 pasar el metodo de la instancia del valor capturado
medicamento_nuevo.asigna_precio(precio)
#medicamento_nuevo.precio  # esto se ingreso, solo para probar

print(f"  el precio es : {medicamento_nuevo.precio}")
print(f"  el descuento es : {medicamento_nuevo.descuento}%")

