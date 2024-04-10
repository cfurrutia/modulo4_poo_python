from ingredientes import lista_proteicos,lista_vegetales, lista_masas

class Pizza():
    #atributos de clase
    tamanio="Familiar"
    precio = 10000

    #paso 2
    @staticmethod
    def validar(elemento,posibles_valores):
        for valor in posibles_valores:
            if valor == elemento.lower():
                return True
        return False
        #return elemento.lower() in posibles_valores

    #paso 3
    def tomar_pedido(self):
        self.proteico = input("Ingrese un ingrediente proteico:\nVacuno\nPollo\nCarne Vegetal\n> ")
        ()
        self.vegetales = []
        self.vegetales.append(input("Ingrese primer ingrediente vegetal:\nTomate\nAceitunas\nChampiñones\n> "))
        ()
        self.vegetal2 = input("Ingrese segundo ingrediente vegetal:\nTomate\nAceitunas\nChampiñones\n> ")
        ()
        self.masa = input("Ingrese tipo de masa:\nTradicional\nDelgada\n> ")
    #paso 4
        self.es_pizza_valida = self.validar(self.proteico,lista_proteicos) and \
        self.validar(self.vegetales[0],lista_vegetales) and \
        self.validar(self.vegetal2,lista_vegetales) and \
        self.validar(self.masa,lista_masas)

    
    
    
    