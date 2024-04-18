#!/usr/bin/python
#-*- coding: utf-8 -*-

class Alternativa:
    def __init__(self, contenido:str, ayuda=""):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativas(self):
        if self.ayuda !="":
            print(self.ayuda)
        return self.contenido

