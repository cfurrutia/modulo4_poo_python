#import pelota
from pelota import Pelota

#INSTANCIAR o CREAR OBJETO
#pelota_de_andy = pelota.Pelota()
pelota_de_andy = Pelota()

print(pelota_de_andy)                    # <pelota.Pelota object at 0x000002442B0B0DD0>
print(type(pelota_de_andy))              # <class 'pelota.Pelota'>
print(pelota_de_andy.forma)              # redondeada
print(pelota_de_andy.material)           

pelota_de_andy.material = "Plastico"
print(pelota_de_andy.material)           # Plastico

pelota_tenis = Pelota()
print(pelota_tenis.material)
pelota_tenis.material = "Caucho"
print(pelota_tenis.posiciones)

# metodos estaticos : no necesita crear una instancia para crear el metodo
print(Pelota.crear_rebote)               # <function Pelota.crear_rebote at 0x000001624561E8E0>
print(Pelota.crear_rebote())             # [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

Pelota.imprimir_posiciones()             
print(Pelota.posiciones)                 # [3, 0, 2, 1, 0]   /  # [2, 4, 6]

Pelota.posiciones = [2,4,6]
Pelota.imprimir_posiciones()
print(Pelota.posiciones)                # [2, 4, 6]

pelota_futbol = Pelota()
print(pelota_futbol.posiciones)

# meotodos no estaticos

pelota_tenis.rebotar()
print(pelota_futbol.posiciones)

pelota_basket = Pelota()
print(pelota_basket.posiciones)
pelota_basket.nuevo_atributo()
print(pelota_basket.color)

# print(pelota_futbol.color)  # AttributeError: 'Pelota' object has no attribute 'color'