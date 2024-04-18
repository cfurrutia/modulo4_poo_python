#!/usr/bin/python
#-*- coding: utf-8 -*-
from pregunta import Pregunta
from usuario import Usuario
class Encuesta:
    def __init__(self, nombre:str, listado_preguntas):
        self.nombre = nombre
        self.__listado_preguntas = [
            Pregunta(pregunta['contenido'],
                    pregunta['ayuda'],
                    pregunta['indicacion'],
                    pregunta['alternativas']) for pregunta in listado_preguntas
            ]
        self.__listado_de_listados_de_respuestas = []

    def mostrar_encuesta(self):
        print(f"Esta encuesta se llama: {self.nombre}")
        for pregunta in self.__listado_preguntas:
            pregunta.mostrar_pregunta()

    def agregar_listado_respuestas(self, respuestas):
        self.__listado_de_listados_de_respuestas.append(respuestas)

class EncuestaPorEdad(Encuesta):
    def __init__(self, edad_minima, edad_maxima):
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, respuestas, edad):
        pass
    
class EncuestaPorRegion(Encuesta):
    def __init__(self):
        self.lista_regiones = None

    def agregar_listado_respuestas(self, respuestas, region):
        pass

