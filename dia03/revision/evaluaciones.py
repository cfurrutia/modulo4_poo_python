from pizza import Pizza

"""
a. Usar la función print(), para que al ejecutar el script se muestre en pantalla los
valores de los atributos de clase de la clase importada, sin crear una instancia
de ella.
"""
#print(Pizza.precio,Pizza.tamanio)
print(f"Las pizzas tienen tamaño {Pizza.tamanio} y su valor es de ${Pizza.precio}.-")

"""
b. Usar la función print(), para que al ejecutar el script se muestre en pantalla
si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de
tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento
2, sin crear una instancia de la clase importada.
"""
print(Pizza.validar("salsa de tomate",["salsa de tomate", "salsa bbq"]))


"""
c. Crear una instancia de la clase importada, y luego llamar al método del
requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de
masa al usuario.
"""
pizza = Pizza()
pizza.tomar_pedido()

"""
d. Usar la función print(), para que al ejecutar el script, luego de que el usuario
haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los
ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia
creada en el paso anterior, y si esa instancia es una pizza válida o no.
"""
if pizza.es_pizza_valida:
    print(f"ingrediente proteico: {pizza.proteico}")
    print(f"ingredientes vejetales: {pizza.vegetales[0]} - {pizza.vegetal2}")
    print(f"La masa seleccionada es: {pizza.masa}")
else:
    print("La pizza no es valida")

"""
e. Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza
válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear
una instancia de la clase. En este punto, la ejecución del script debe mostrar
un error (todos los pasos anteriores se deben haber ejecutado correctamente).
"""
print(Pizza.es_pizza_valida)
#AttributeError: type object 'Pizza' has no attribute 'es_pizza_valida'