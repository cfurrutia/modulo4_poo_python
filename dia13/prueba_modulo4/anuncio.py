from abc import ABC, abstractmethod
from error import SubTipoInvalidoError
class Anuncio(ABC):
    # Definir atributos de clase FORMATOS y SUB_TIPOS
    FORMATOS = ()
    SUB_TIPOS = ()
    # Definir el constructor de la clase Anuncio con atributos alto, ancho, url_archivo, url_clic y sub_tipo
    def __init__(self, alto: int, ancho: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__sub_tipo = sub_tipo
        self.__alto = alto
        self.__ancho = ancho
        self.__url_clic = url_clic
        self.__url_archivo = url_archivo
        self.__sub_tipo = sub_tipo
    # Definir propiedades para acceder a sub_tipo, alto, ancho, url_clic y url_archivo
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
    @alto.setter
    def url_clic(self, alto):
        self.__url_clic = alto
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__url_clic = ancho
    
    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    # Definir métodos abstractos comprimir_anuncio y redimensionar_anuncio
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    # Definir un método estático mostrar_formatos para mostrar los formatos y subtipos disponibles
    @staticmethod
    def mostrar_formatos(FORMATOS, SUB_TIPOS):
        print(f"{FORMATOS}:")
        print("===========")
        for subtipo in SUB_TIPOS:
            print(f"- {subtipo}")

# Definir la clase Video que hereda de Anuncio
class Video(Anuncio):
    # Definir atributos de clase FORMATOS y SUB_TIPOS específicos para Video
    FORMATOS = ("Video")
    SUB_TIPOS = ("instream", "outstream")

    # Definir el constructor de Video con sub_tipo y duracion
    def __init__(self, sub_tipo, duracion):
        super().__init__(1, 1, '', '', sub_tipo) 
        self.__duracion = duracion

    # Definir propiedades para acceder y modificar la duracion
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        self.__duracion = nueva_duracion if nueva_duracion > 0 else 5
    
    # Definir métodos comprimir_anuncio y redimensionar_anuncio para Video
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

# Definir la clase Display que hereda de Anuncio
class Display(Anuncio):
    # Definir atributos de clase FORMATOS y SUB_TIPOS específicos para Display
    FORMATOS = ("Display")
    SUB_TIPOS = ("tradicional", "nativo")

    # Definir métodos comprimir_anuncio y redimensionar_anuncio para Display
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

# Definir la clase Social que hereda de Anuncio
class Social(Anuncio):
    # Definir atributos de clase FORMATOS y SUB_TIPOS específicos para Social
    FORMATOS = ("Social")
    SUB_TIPOS = ("facebook", "linkedin")

    # Definir métodos comprimir_anuncio y redimensionar_anuncio para Social
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

# Verificar si el script se está ejecutando como el programa principal
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