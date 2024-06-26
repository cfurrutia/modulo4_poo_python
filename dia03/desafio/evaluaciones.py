from pizza import Pizza
import os
os.system("cls" if os.name == "nt" else "clear") # limpiar la pantalla del terminal

# Menu ingredientes posibles
print("Por favor, elige los ingredientes para tu pizza \n") 
print("Ingredientes proteicos posibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales posibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa posibles:", Pizza.tipos_masa)
# validacion de entrada de salsa de tomate
print("¿Salsa de tomate está presente en la lista? \n", Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))
# Crear una instancia de la clase Pizza
pizza = Pizza()

# Realizar un pedido
pizza.realizar_pedido()

# Mostrar los ingredientes y tipo de masa del pedido
print("Ingredientes vegetales:", pizza.primer_ingrediente_vegetal, pizza.segundo_ingrediente_vegetal)
print("Ingrediente proteico:", pizza.ingrediente_proteico)
print("Tipo de masa:", pizza.tipo_masa)

# Verificar si el pedido es válido
print("¿Es una pizza válida? \n","si" if pizza.es_pizza_valida else "no")
# Verificar si la clase Pizza es una pizza válida
try:
    print("¿Es la clase Pizza una pizza válida? \n", "si" if Pizza.es_pizza_valida else "no")
except AttributeError:  # captura y maneja la excepción AttributeError
    print("¿Es la clase Pizza una pizza válida? \n", "no")