from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):

    # Definir el constructor de la clase Anuncio con atributos alto, ancho, url_archivo, url_clic y sub_tipo
    def __init__(self, alto: int, ancho: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__alto = alto if alto > 0 else 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1
    
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @ancho.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo   
    
    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def alto(self, url_clic):
        self.__url_clic = url_clic    
            
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        """
        if (isinstance(self,Video)and sub_tipo not in Video.SUB_TIPOS or isinstance(self,Display)and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self,Social)and sub_tipo not in Social.SUB_TIPOS):
        """
        if (sub_tipo in self.SUB_TIPOS):
            raise SubTipoInvalidoError("El subtipo no es válido.")
        else:
            self.__sub_tipo=sub_tipo
        
    # Definir un método estático mostrar_formatos para mostrar los formatos y subtipos disponibles
    @staticmethod
    def mostrar_formatos():
        print("Video :")
        print("===========")
        for subtipo in Video.SUB_TIPOS:
            print(f"- {subtipo}")
        
        print("Display :")
        print("===========")
        for subtipo in Display.SUB_TIPOS:
            print(f"- {subtipo}")
    
        print("Social :")
        print("===========")
        for subtipo in Social.SUB_TIPOS:
            print(f"- {subtipo}")
            
    # Definir métodos abstractos comprimir_anuncio y redimensionar_anuncio
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

# Definir la clase Video que hereda de Anuncio
class Video(Anuncio):
    # Definir atributos de clase FORMATOS y SUB_TIPOS específicos para Video
    FORMATOS = ("Video")
    SUB_TIPOS = ("instream", "outstream")

    # Definir el constructor de Video con sub_tipo y duracion
    def __init__(self,url_archivo: str, url_clic: str, sub_tipo: str,duracion: str):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__alto = 1
        self.__ancho = 1
        self.__duracion = duracion

    # Definir propiedades para acceder y modificar la duracion
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        pass
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        pass
    
    # Definir métodos comprimir_anuncio y redimensionar_anuncio para Video
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

# Definir la clase Display que hereda de Anuncio
class Display(Anuncio):
    # Definir atributos de clase FORMATOS y SUB_TIPOS específicos para Display
    FORMATOS = ("Display")
    SUB_TIPOS = ("tradicional", "native")
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(url_archivo, url_clic, sub_tipo)
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
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(url_archivo, url_clic, sub_tipo)
    # Definir métodos comprimir_anuncio y redimensionar_anuncio para Social
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

# Verificar si el script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Prueba de Video
    test= Video("","","",0)
    test.alto = 720
    print(test.alto)
    test.sub_tipo = "test subtipo"
