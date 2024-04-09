from te import Te # Importa la clase Te desde el módulo te
import os

os.system("cls" if os.name == "nt" else "clear") # limpiar la pantalla del terminal

# Solicitar al usuario los datos del pedido
sabor = int(input("Ingrese el sabor de té que desea (1: Té negro, 2: Té verde, 3: Agua de hierbas):  \n"))
formato = int(input("Ingrese el formato de té que desea (300 para 300 gr, o 500 para 500 gr): \n"))

# Obtener los valores necesarios para el pedido utilizando los métodos de la clase te
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Mostrar el detalle del té ordenado
print(f"Detalle del pedido")
print(f"Usted eligió la opción: {sabor}")
if sabor == 1:
    print("Té negro")
elif sabor == 2:
    print("Té verde")
elif sabor == 3:
    print("Agua de hierbas")
print(f"Formato: {formato} gr")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")


