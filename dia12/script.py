from usuario import Usuario
import json

lista_usuarios = [] #lista vacía para almacenar instancias
try:
    with open("dia12/usuarios.txt", "r") as usuarios: #abrir archivo en modo lectura con un alias
        for linea in usuarios.readlines(): #recorrer por línea el archivo con todas sus líneas
            try: #control de excepciones
                datos_linea = json.loads(linea) #convertir línea de texto en diccionario y guardarlo en una variable
                #se crea una instancia de Usuario con los parámetros desde datos_linea y se almacenan en lista_usuarios
                lista_usuarios.append(Usuario)
            except Exception as e: #en caso de haber un error se le da un alias
                with open(f"dia12/logs/error_usuario.log", "a+",encoding="utf-8") as usuariolog: #y se escribe en error.log cuál fue el error
                    usuariolog.write(f"Error al procesar la línea: {linea}\tExcepción: {e}\n")
                print("Ha habido un error:", e ) #también se imprime dicho error por consola
            else:
                print(f"Usuario creado: {datos_linea.get("nombre")} {datos_linea.get("apellido")}") #si no hay errores, imprime el usuario creado con su nombre y apellido
                
except Exception as error: #prueba, en caso de no estar el archivo lanza este error
    with open(f"dia12/logs/error_archivo.log", "a+",encoding="utf-8") as archivolog:
        archivolog.write(f"Error al abrir el archivo.\n\tExcepción: {error}\n")
    archivolog.close()
finally:    
    usuarios.close()
    usuariolog.close()    