from pelota import Pelota

# Se crea instancia, creacion del objeto 
pelota_multicolor = Pelota()
# Se asigna color a la instancia
pelota_multicolor.asigna_color("rojo")
# Se lee color. La salida será "El color de esta pelota es rojo"
pelota_multicolor.lee_color()
pelota_multicolor.asigna_color("verde")
# Las salidas serán:
# El color de esta pelota es verde
# El color amarillo NO es el color de ESTA pelota
pelota_multicolor.lee_color_local_y_atributo("amarillo")

pelota_negra = Pelota()
pelota_negra.lee_color_local_y_atributo("Negro")