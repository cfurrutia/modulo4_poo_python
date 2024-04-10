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
pizza.realizar_pedido()

# Mostrar los ingredientes y tipo de masa del pedido
print("\n Ingredientes vegetales:", pizza.ingrediente_vegetal1, ",", pizza.ingrediente_vegetal2)
print("Ingrediente proteico:", pizza.ingrediente_proteico)
print("Tipo de masa:", pizza.tipo_masa)
print("¿Es una pizza válida? \n","si" if pizza.es_valida else "no")
#mostrar en pantalla si la clase Pizza es una pizza válida o no  
print("¿Es la clase Pizza una pizza válida? \n", "si" if Pizza().es_valida else "no")


