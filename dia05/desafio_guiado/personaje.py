#personaje.py
class Personaje:
    # Definimos el método constructor
    def __init__(self, nombre):
        # Inicializa los atributos del personaje
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
    # Definimos un método para retornar el estado del personaje como una cadena
    def __str__(self):
        # Retorna una cadena con el estado del personaje
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    # Definimos un método para asignar experiencia al personaje
    def asignar_estado(self, experiencia):  # Método para actualizar el estado del personaje
        self.experiencia += experiencia  
        while self.experiencia >= 100:  
            self.nivel += 1  
            self.experiencia -= 100  
        while self.experiencia < 0:  
            if self.nivel > 1: 
                self.nivel -= 1  
                self.experiencia += 100  
            else:
                self.experiencia = 0

    # Definimos un método de comparación para "menor que"
    def __lt__(self, other):
        # Método de comparación para "menor que"
        return self.nivel < other.nivel

    # Definimos un método de comparación para "mayor que"
    def __gt__(self, other):
        # Método de comparación para "mayor que"
        return self.nivel > other.nivel

    # Definimos un método para calcular la probabilidad de ganar contra otro personaje
    def probabilidad_ganar(self, other):
        # Calcula la probabilidad de ganar contra otro personaje
        return 0.33 if self < other else (0.66 if self > other else 0.5)

    # Definimos un método estático para mostrar un diálogo de enfrentamiento y retornar la opción elegida por el jugador
    @staticmethod
    def enfrentamiento_dialogo(probabilidad):
        # Muestra un diálogo de enfrentamiento y retorna la opción elegida por el jugador
        print(f"¡Oh no!, ¡Ha aparecido un Orco!\nCon tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("\n¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        opcion = int(input())
        return opcion

