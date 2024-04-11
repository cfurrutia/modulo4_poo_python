# constructores ,  lo que hace es incializar valores de atributo
# Es un método que se ejecuta automáticamente al momento de crear una instancia de 
# la clase, sin necesidad de ser llamado explícitamente. 

class Pelota():
    # Metodo constructor al crear el objeto    
    def __init__(self, color: str, tamanio= 20, material= "plástico"):   
        print("¡Se ha creado una pelota!")  
        self.__color = color
        self.tamanio = tamanio
        self.material = material
        self.rebotes = 0
        
    # Metodo oculto
    def __getcolor(self):
        return self.__color    
    
    def setcolor(self, color):
        self.__color = color      
        
    def setpassword(self, password):
        self.__password = password
        
    # getter
    @property
    def color(self):
        return self.__color
    #setter
    @color.setter
    def color(self,color: str):
        self.__color = color
        self.__color = color if color != "" else "Verde"    
        
        
# Salida: "¡Se ha creado una pelota!"
#pelota_futbol = Pelota("Amarillo", 16, "plástico")

#print("metodo getter", pelota_futbol.color)
# Salida: blanco 20 plástico
#print(pelota_futbol.color, pelota_futbol.tamanio, pelota_futbol.material)

# pelota3 = Pelota(0, material= "plástico")
# print(pelota3.color, pelota3.tamanio, pelota3.material)
# pelota3.rebotes=10
# pelota4 = Pelota()



