#!/usr/bin/python
#-*- coding: utf-8 -*-
from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado=None, ayuda=None, indicacion=False, alternativas=[]):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.indicacion = indicacion
        self.__alternativas = [
            Alternativa(alternativa['contenido'], alternativa['ayuda']) for alternativa in alternativas
            ]
    def mostrar_pregunta(self):
        print("Enunciado:", self.enunciado)
        if self.indicacion==True:
            print("Ayuda:", self.ayuda)
        print("Alternativas:")
        for alternativa in self.__alternativas:
            alternativa.mostrar_alternativa()
