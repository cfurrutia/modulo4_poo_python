""" 
ABSTRACCION:
Una Clase es abstracta, si tiene a lo menos un metodo abstracto
Metodo Abstracto: son aquellos que tienen solo la definicion del metodo

para poder crear una clase abstracta y un metodo abstracto importamos:

from abc import ABC, abstractmethod

"""

from abc import ABC, abstractclassmethod

class Pelota(ABC):
    
    # definicion del metodo abstracto
    @abstractclassmethod
    def rebotar(self):
        pass
    
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.color = "Blanco"    
        
    def rebotar(self, altura: int):
        pass
    
    def imprimir(self):
        print("metodo de la subclase")    
        
#creacion de objeto
pelotita = PelotaDeJuguete()
print(pelotita.rebotar(20))