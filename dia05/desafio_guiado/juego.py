# integrantes Jimena Traipe, Diego Larena, Carlos Urrutia, Flavia Cayun, Yessenia Millar


import random #para generar números aleatorios
from personaje import Personaje#Importamos la clase Personaje del módulo personaje

# Definimos una clase llamada Juego
class Juego:
    def __init__(self, jugador: Personaje, orco: Personaje):
        self.jugador = jugador
        self.orco = orco
    # Definimos un método estático llamado jugar

    def jugar(self):
        
        # Calculamos la probabilidad de que el jugador gane contra el orco
        probabilidad_ganar = self.jugador.probabilidad_ganar(self.orco)

        # Mostramos el diálogo de enfrentamiento y obtenemos la elección del jugador
        opcion = self.jugador.enfrentamiento_dialogo(probabilidad_ganar)

        # Continuamos el juego hasta que el jugador elija huir
        while opcion == 1:
            resultado_ataque = "Gana" if random.uniform(0, 1) <= probabilidad_ganar else "Pierde"
            if resultado_ataque == "Gana":
                print("\nLe has ganado al orco, felicidades!")
                print("¡Recibirás 50 puntos de experiencia!")
                self.jugador.asignar_estado(50)
                self.orco.asignar_estado(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                print("¡Has perdido 30 puntos de experiencia!")
                self.jugador.asignar_estado(-30)
                self.orco.asignar_estado(50)
            # Imprimimos el estado actual de ambos personajes    
            print(self.jugador)
            # Recalculamos la probabilidad de ganar
            print(self.orco)
            probabilidad_ganar = self.jugador.probabilidad_ganar(self.orco)
            # Mostramos el diálogo de enfrentamiento nuevamente y obtenemos la nueva elección del jugador
            opcion = self.jugador.enfrentamiento_dialogo(probabilidad_ganar)
        
        # Si el jugador elige huir, imprimimos un mensaje de despedida
        print("¡Has huido! El orco ha quedado atrás.")

if __name__ == "__main__":
        
    # Iniciamos del juego
    print("Bienvenido a Gran Fantasia!")#mensaje de bienvenida
    # Pedimos al usuario el nombre de su personaje
    nombre_personaje = input("Por favor indique nombre de su personaje:\n")
    # Creamos un nuevo objeto Personaje con el nombre dado
    jugador = Personaje(nombre_personaje)
    print(jugador)#estado actual del personaje del jugador

    # Creamos un nuevo objeto Personaje llamado "Orco"
    orco = Personaje("Orco")
    juego = Juego(jugador,orco)
    juego.jugar()    

