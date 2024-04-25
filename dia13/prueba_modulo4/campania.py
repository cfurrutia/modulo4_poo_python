from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campania:
    def __init__(self, nombre, anuncios, fecha_inicio, fecha_termino):
        self.nombre = nombre
        self.__anuncios = self.crear_anuncios(anuncios)
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino

    def crear_anuncios(self, anuncios):
        anuncios_creados = []
        for anuncio in anuncios:
            tipo = anuncio['tipo']
            sub_tipo = anuncio['sub_tipo']
            if tipo == 'Video':
                duracion = anuncio['duracion']
                anuncios_creados.append(Video(sub_tipo, duracion))
            elif tipo == 'Display':
                anuncios_creados.append(Display(1, 1, '', '', sub_tipo))  
            elif tipo == 'Social':
                anuncios_creados.append(Social(sub_tipo))
        return anuncios_creados

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) <= 250:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoError("El nombre de la campaña no puede superar los 250 caracteres.\n")

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self.__fecha_inicio = nueva_fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        self.__fecha_termino = nueva_fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        contadores = {'Video': 0, 'Display': 0, 'Social': 0}
        for anuncio in self.__anuncios:
            tipo = type(anuncio).__name__
            contadores[tipo] += 1

        resultado = f"Nombre de la campaña: {self.nombre}\nAnuncios: "
        for tipo, cantidad in contadores.items():
            resultado += f"{cantidad} {tipo}, "
        return resultado[:-2]
