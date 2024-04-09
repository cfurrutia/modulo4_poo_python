class Pelota():
    #atribute
    pass
    forma ="redondeada"    # atributo estatico o atributo de clase
    material =""

    posiciones = [3, 0, 2, 1, 0]
    @staticmethod
    def crear_rebote():
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)

# metodo no estatico o de instancia, siempre van con self

    def rebotar(self):
        self.posiciones = self.crear_rebote()
        
# metodo no estaticos

    def rebotar(self):
        self.posiciones = self.crear_rebote()
        
    def nuevo_atributo(self):
        self.color = "blanco"           