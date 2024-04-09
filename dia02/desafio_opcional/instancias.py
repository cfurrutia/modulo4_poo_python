from te import Te  # Importamos la clase Te desde el módulo te

# Crear dos instancias de la clase Te y almacenar el tipo de dato de cada instancia en una variable (enteras)
instanciate1 = type(Te())
instanciate2 = type(Te())

# Mostrar el valor de cada tipo de dato
print("Tipo de instancia 1:", instanciate1)
print("Tipo de instancia 2:", instanciate2)


# Verificar si los tipos de datos son iguales
if instanciate1 == instanciate2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
    

