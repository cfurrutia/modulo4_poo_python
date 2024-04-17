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
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):  #se define la clase abstracta 
        self.__correo_suscriptor = correo_suscriptor   #incluye un constructor que genera los dos atributos de instancia
        self.__numero_tarjeta = numero_tarjeta   #por pauta son métodos privados
    costo = 0 #atributos de clase para heredar
    cant_dispositivos = 0
    @abstractmethod
    def cambiar_suscripcion(self): #métodos abstractos que DEBEN ser implementados en cada subclase
        pass
    
    @abstractmethod
    def cancelar_suscripcion(self):
        pass 

    @property #getter de correo
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    
    @property #getter de numero tarjeta
    def numero_tarjeta(self):
        return self.__numero_tarjeta
        
class Gratis(Membresia):  #clase Gratis es hija de Membresia, por lo que hereda todo lo que tiene
    __cant_dispositivos = 1 #se modifica el atributo heredado, privado y sin propiedades para evitar la modificación
    #constructor es heredado, opté por no incluirlo
    def __crear_nueva_membresia(self, correo_suscriptor, numero_tarjeta): #método para crear membresías, exclusivo de gratis
        g = Gratis(correo_suscriptor,numero_tarjeta) #genera un objeto de tipo gratis con los parámetros reqeuridos por la clase membresía
    def cambiar_suscripcion(self, tipo_suscripcion): #método para modificar el tipo de suscripción, recibe un int como parámetro
        lista_tipos=[1,2,3,4]
        if tipo_suscripcion in lista_tipos: #identifica si el número ingresado es parte de las opciones
            if tipo_suscripcion == 1: #según cada número ls suscripción cambiará
                return Basica(self.correo_suscriptor, self.numero_tarjeta) #retornando la estructura para que una variable se vuelva objeto
            elif tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta) #aprovechando que el objeto g tiene acceso al correo y número de tarjeta
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4" #validación del error
    def cancelar_suscripcion(self):
        pass #no se cancelan membresías gratuitas
    @property
    def crear_nueva_membresia(self): #getter
        return self.__crear_nueva_membresia 
    
class Basica(Membresia): #nueva clase
    __costo = 3000
    __cant_dispositivos = 2 #modificación de atributos
#nuevamente no incluyo el constructor, usa el mismo que Membresía
    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[2,3,4] #lista modificada, no incluye su propio número
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta) #mismo proceso con las otras 3 clases de membresía
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)

        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta) #si cancelan suscripción, pasan a membresía gratis

class Familiar(Basica):
    __costo = 5000 #modificación de atributos
    __cant_dispositivos = 5

    def __init__(self, correo_suscriptor: str, numero_tarjeta: int, dias_gratis=7): #inclusión de dias gratis en el constructor heredado
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_gratis = dias_gratis #definición del atributo a partir del parámetro, privado para que no sea modificado externamente

    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[1,3,4] #lista de tipos que no son familiar
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 1:
                return Basica(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 3:
                return SinConexion(self.correo_suscriptor, self.numero_tarjeta) # idem 
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta) #idem
    
    def control_parental(self): #se incluye el método de control parental que aún no está implementado, se heredará a sus clases hijas
        pass
    



class SinConexion(Basica):
    __costo = 3500 #atributos modificados
    __cant_dispositivos = 2
    def __init__(self, correo_suscriptor: str, numero_tarjeta: int, dias_gratis=7): #misma modificación del constructor
        super().__init__(correo_suscriptor, numero_tarjeta) #con constructor heredado
        self.__dias_gratis = dias_gratis #y atributo definido por parámetro
    def cambiar_suscripcion(self, tipo_suscripcion):
        lista_tipos=[1,2,4] #lista de tipos que no son SinConexion
        if tipo_suscripcion in lista_tipos:
            if tipo_suscripcion == 1:
                return Basica(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 2:
                return Familiar(self.correo_suscriptor, self.numero_tarjeta)
            elif tipo_suscripcion == 4:
                return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return "El tipo de membresía debe ser un número entero entre 1 y 4"
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    
    def contenido_adicional(self): #se establece un método para obtener contenido adicional sin conexión, aún no se implemeta, pero se heredará
        pass

class Pro(Familiar, SinConexion):
    __costo = 7000 #modificación de atributos
    __cant_dispositivos = 6
    def __init__(self, correo_suscriptor: str, numero_tarjeta: int, dias_gratis=15): #más días gratis por defecto
        super().__init__(correo_suscriptor, numero_tarjeta, dias_gratis) #el constructor cambia, llama al de Familiar (MRO)
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
    g = Gratis("correo@prueba.cl", "123 456 789") #Validación con un objeto creado como Gratis
    print(type(g)) #<class '__main__.Gratis'>
    b = g.cambiar_suscripcion(1) #que cambia a Básico
    print(type(b)) #<class '__main__.Basica'>     
    f = b.cambiar_suscripcion(2) #luego a Familiar
    print(type(f)) #<class '__main__.Familiar'>   
    sc = f.cambiar_suscripcion(3) #De familiar a SinConexion
    print(type(sc)) # <class '__main__.SinConexion'>
    pro = sc.cambiar_suscripcion(4) #De SinConexion a Pro
    print(type(pro)) # <class '__main__.Pro'>   
    g2 = pro.cancelar_suscripcion() #Luego cancela su suscripción y queda como Gratis
    print(type(g2)) # <class '__main__.Gratis'>   
