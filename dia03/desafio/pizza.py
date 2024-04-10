class Pizza:
# Atributos de clase - ingredientes
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        """Método para validar un elemento en una lista de casos posibles
        Args:
            elemento (_type_): Elemento a validar
            valores_posibles (lista): Lista de valores posibles
        Returns:
            bool : True si el elemento es válido, False en caso contrario
        """
        return elemento in valores_posibles
    
    def realizar_pedido(self):
        """Método para realizar un pedido
        """
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa : ")
            
        #  Verificar si el pedido es válido
        self.es_valida = self.validar_elemento(self.ingrediente_proteico, self.ingredientes_proteicos) and \
        self.validar_elemento(self.ingrediente_vegetal1, self.ingredientes_vegetales) and \
        self.validar_elemento(self.ingrediente_vegetal2, self.ingredientes_vegetales) and \
        self.validar_elemento(self.tipo_masa, self.tipos_masa)
        
    
# prueba de pedidos   ( __init__, metodo especial,constructor de una clase)
    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False         
   
