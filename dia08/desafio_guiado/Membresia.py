""" 
Carlos Urrutia
Jimena Traipe
Flavia Cayún
Yessenia Millar
Matías Valdivia
Diego Larenas
"""

from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta
    costo = 0
    cant_dispositivos = 0
    @abstractmethod
    def cambiar_suscripcion(self):
        pass
    
    @abstractmethod
    def cancelar_suscripcion(self):
        pass 

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
        
class Gratis(Membresia):
    __cant_dispositivos = 1
    def __init__(self, correo_suscriptor: str, numero_tarjeta: int):
        super().__init__(correo_suscriptor, numero_tarjeta)
    def __crear_nueva_membresia(self, correo_suscriptor, numero_tarjeta):
        g = Gratis(correo_suscriptor,numero_tarjeta)
    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[1,2,3,4]
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 1:
                return Basica(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    def cancelar_suscripcion(self):
        pass
    @property
    def crear_nueva_membresia(self):
        return self.__crear_nueva_membresia 
    
class Basica(Membresia):
    __costo = 3000
    __cant_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: int):
        super().__init__(correo_suscriptor, numero_tarjeta)

    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[2,3,4]
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)

        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
class Familiar(Basica):
    __costo = 5000
    __cant_dispositivos = 5

    def __init__(self, correo_suscriptor: str, numero_tarjeta: int, dias_gratis=7):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_gratis = dias_gratis

    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[1,3,4]
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 1:
                return Basica(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)

        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    def control_parental(self):
        pass
    



class SinConexion(Basica):
    __costo = 3500
    __cant_dispositivos = 2
    def __init__(self, correo_suscriptor: str, numero_tarjeta: int, dias_gratis=7):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_gratis = dias_gratis
    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[1,2,4]
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 1:
                return Basica(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta,7)
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta,15)
        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    
    def contenido_adicional(self):
        pass

class Pro(Familiar, SinConexion):
    __costo = 7000
    __cant_dispositivos = 6
    def __init__(self, correo_suscriptor: str, numero_tarjeta: int, dias_gratis=15):
        super().__init__(correo_suscriptor, numero_tarjeta, dias_gratis)
        self.__dias_gratis = dias_gratis

    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[1,2,3]
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 1:
                return Basica(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta,7)
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta,7)
        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
        

if __name__ == "__main__":
    g = Gratis("correo@prueba.cl", "123 456 789")
    print(type(g)) #<class '__main__.Gratis'>
    b = g.cambiar_suscripcion(1)
    print(type(b))
    f = b.cambiar_suscripcion(2)
    print(type(f))
    sc = f.cambiar_suscripcion(3)
    print(type(sc))
    pro = sc.cambiar_suscripcion(4)
    print(type(pro))
    g2 = pro.cancelar_suscripcion()
    print(type(g2))
