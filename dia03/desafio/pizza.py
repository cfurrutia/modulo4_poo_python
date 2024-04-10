# Clase Pizza
class Pizza:
    # Atributos de clase
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]

    # Método para validar un elemento en una lista de casos posibles
    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        """Método para validar un elemento en una lista de casos posibles

        Args:
            elemento (any): Elemento a validar
            valores_posibles (lista): Lista de valores posibles

        Returns:
            bool : True si el elemento es válido, False en caso contrario
        """
        if elemento in valores_posibles:
            return True
        else:
            return False
        
    def realizar_pedido(self):
        """Método para realizar un pedido
        """
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.primer_ingrediente_vegetal = input("Ingrese el primer ingrediente vegetal: ")
        self.segundo_ingrediente_vegetal = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa: ")

    
        self.es_pizza_valida = self.validar_elemento(self.ingrediente_proteico, self.ingredientes_proteicos) and \
        self.validar_elemento(self.primer_ingrediente_vegetal, self.ingredientes_vegetales) and \
        self.validar_elemento(self.segundo_ingrediente_vegetal, self.ingredientes_vegetales) and \
        self.validar_elemento(self.tipo_masa, self.tipos_masa)
