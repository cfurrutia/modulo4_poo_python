from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    FORMATOS = ()
    SUB_TIPOS = ()

    def __init__(self, sub_tipo):
        self.__sub_tipo = sub_tipo
        self.__alto = 1
        self.__ancho = 1
        self.__url_clic = ""
        self.__url_archivo = ""

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if nuevo_sub_tipo in self.SUB_TIPOS:
            self.__sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoError("El subtipo no es válido.")

    @property
    def alto(self):
        return self.__alto

    @property
    def ancho(self):
        return self.__ancho
    
    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, nueva_url_clic):
        self.__url_clic = nueva_url_clic

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, nueva_url_archivo):
        self.__url_archivo = nueva_url_archivo

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass
            
            
    @staticmethod
    def mostrar_formatos(FORMATOS, SUB_TIPOS):
        print(f"{FORMATOS}:")
        print("==========")
        for subtipo in SUB_TIPOS:
            print(f"- {subtipo}")
            

class Video(Anuncio):
    FORMATOS = ('Video')
    SUB_TIPOS = ('instream', 'outstream')

    def __init__(self, sub_tipo, duracion):
        super().__init__(sub_tipo)
        self.__duracion = duracion

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        self.__duracion = nueva_duracion if nueva_duracion > 0 else 5
    
    @property
    def alto(self):
        return self.__alto

    @property
    def ancho(self):
        return self.__ancho

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATOS = ('Display')
    SUB_TIPOS = ('tradicional', 'nativo')

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATOS = ('Social')
    SUB_TIPOS = ('facebook', 'linkedin')

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

if __name__ == "__main__":
    
    # Prueba de Anuncio
    print("Anuncio:\n")
    # Prueba de Video
    Video.mostrar_formatos(Video.FORMATOS, Video.SUB_TIPOS)
    print()
    # Prueba de Display
    Display.mostrar_formatos(Display.FORMATOS, Display.SUB_TIPOS)
    print()
    # Prueba de Social
    Social.mostrar_formatos(Social.FORMATOS, Social.SUB_TIPOS)