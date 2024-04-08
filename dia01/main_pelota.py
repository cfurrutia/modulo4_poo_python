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


