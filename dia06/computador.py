# Esta clase define un tipo de memoria RAM con dos atributos: velocidad y bite.
class Ram():
    def __init__(self, velocidad: int, bite: int):
        self.velocidad = velocidad
        self.bite = bite

# Esta clase define un teclado con dos atributos: idioma y cant_teclas.        
class Teclado():
    def __init__(self, idioma: str, cant_teclas: int):
        self.idioma = idioma
        self.cant_teclas = cant_teclas

# Esta clase define un mouse con dos atributos: tipo y conectividad.        
class Mouse():
    def __init__(self, tipo : str, conectividad: str):   
        self.tipo =tipo
        self.conectividad=conectividad     
# Esta clase define un disco duro con un atributo: capacidad. Además, tiene un atributo privado __tipo que no se puede acceder directamente desde fuera de la clase.        
class DiscoDuro():
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.__tipo = "ssd"

"""
Esta clase define un computador con cuatro atributos: ram, disco_duro, teclado, y mouse. La ram es una instancia de la clase Ram y se inicializa con los argumentos 
velocidad_ram y bite. El disco_duro es una instancia de la clase DiscoDuro y se inicializa con el argumento capacidad_dd.
Los atributos teclado y mouse son instancias de las clases Teclado y Mouse, respectivamente, y se inicializan con los argumentos correspondientes. 
"""
class Computador():
    def __init__(self, teclado: Teclado, mouse: Mouse, velocidad_ram: int, capacidad_dd: int):
        self.ram = Ram(velocidad_ram,32)
        self.disco_duro = DiscoDuro(capacidad_dd)
        
        self.teclado = teclado
        self.mouse = mouse
        
# Se crean instancias de las clases Teclado y Mouse con los argumentos correspondientes.        
teclado = Teclado("Latino",120)
mouse = Mouse("Gamer", "bluetooth")
# Se crea una instancia de la clase Computador con las instancias teclado y mouse y los argumentos velocidad_ram y capacidad_dd.        
computador_gamer = Computador(teclado, mouse,2300, 500)
# Se imprimen los valores de la velocidad de la RAM y la cantidad de teclas del teclado del computador.
print(computador_gamer.ram.velocidad)
print(computador_gamer.teclado.cant_teclas)