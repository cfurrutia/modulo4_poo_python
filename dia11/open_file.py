# Función para abrir un archivo con el modo de apertura especificado
# Se asume que 'ruta' es la ruta del archivo y 'argumento' es el modo de apertura
# def file(open, ruta, argumento o modo de apertura)

# Importar el módulo os
import os

try:
    # Intentar abrir el archivo de registro (log)
    log_file = open(os.path.abspath("dia11/logs/error.log"))
    print(log_file)
    print(type(log_file))
except FileNotFoundError as fnfe:
    # Si el archivo no se encuentra, imprimir un mensaje de error
    print("archivo o directorio no encontrado")
    print(fnfe)

# Leer el contenido del archivo index.html y mostrarlo
print("**************READ*************\n")
log_file2 = open(os.path.abspath("dia11/html/index.html"), "r")
print(log_file2.read())
log_file2.close()

# Leer una sola línea del archivo index.html y mostrarla
print("******************READLINE*********\n")
log_file3 = open(os.path.abspath("dia11/html/index.html"), "r")
print(log_file3.readline)
log_file3.close()

# Leer todas las líneas del archivo index.html y mostrarlas
print("******************READLINES*********\n")
log_file4 = open(os.path.abspath("dia11/html/index.html"), "r")
print(log_file4.readlines)
log_file4.close()

# Abrir y leer el contenido del archivo index.html usando 'with' statement
print("******************WHTH*********\n")
with open(os.path.abspath("dia11/html/index.html"), "r") as archivo:
    # Imprimir cada línea del archivo sin espacios en blanco alrededor
    for linea in archivo:
        print(linea.strip())

# Abrir el archivo style.css en modo escritura y escribir en él
log_file5 = open(os.path.abspath("dia11/html/assets/css/style.css"), "w")
log_file5.write("/*Esto es un comentario*/")
log_file5.write(" * {margin: 0px}")
log_file5.close()

# Importar el módulo time
import time

try:
    # Imprimir la marca de tiempo actual y la versión redondeada
    print(time.time())
    print(round(time.time()))
    # Solicitar al usuario que ingrese su edad
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    # Si ocurre un error, registrar el error en un archivo de registro con una marca de tiempo única
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
