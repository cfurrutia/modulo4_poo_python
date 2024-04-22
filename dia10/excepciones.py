"""
class MisExcepciones(Exception):
    def imprimir_promedio(self,dividendo, divisor):
        promedio = dividendo/divisor #ZeroDivisionError: division by zero
        print(f"El promedio es: {promedio}")
calculo_promedio = MisExcepciones()
calculo_promedio.imprimir_promedio(100,0)
"""
class Error(Exception):
    pass

class DivisorError(Error):
    def __init__(self, mensaje, divisor):
        self.divisor = divisor
        self.mensaje = mensaje

class MisExcepciones(Exception):

    def imprimir_promedio(self,dividendo, divisor):
        try:
            promedio = dividendo/divisor #ZeroDivisionError: division by zero
            print(f"El promedio es: {promedio}")
        except ZeroDivisionError:
            print("ERROR:: El divisor no puede ser un cero")
        #captura generica de una excepcion
        except Exception as error:
            print("ERROR:: Se ha producio un error:", error)
        finally:
            print("El metodo se ha ejecutado\n")

calculo_promedio = MisExcepciones()
valido = True

while valido:
    try:
        dividendo = int(input("ingrese el numero dividendo > "))
        valido = False
    except ValueError:
        print("Error en el ingreso del dividendo")

valido = True

while valido:
    try:
        divisor = int(input("ingrese el numero divisor > "))
        if divisor == 0:
            raise DivisorError("Divisor no puede ser cero",divisor)
        
        break#forzar la salida inmediata del while(no pasa por finally) #valido = False
    except DivisorError as de:
        print("Error en el ingreso del divisor:: ",de.mensaje)
    except ValueError:
        print("Error en el ingreso del divisor")
    except Exception as error:
            print("Se ha producio un error:", error) 
    finally:#SIEMPRE SE EJECUTARA FINALLY
        pass


calculo_promedio.imprimir_promedio(dividendo,divisor)

print("Gracias por participar en clases")