from campania import Campania
from error import LargoExcedidoError, SubTipoInvalidoError

try:
    # Crear una instancia de Campaña con un anuncio de tipo Video
    anuncios = [{'tipo': 'Video', 'sub_tipo': 'outstream', 'duracion': 4}]
    # Crear la instancia de Campania
    campania = Campania("Campaña de prueba", anuncios)
    # Imprimir la representación de la campaña
    print(campania)
    # Solicitar al usuario que ingrese un nuevo nombre para la campaña
    nuevo_nombre = input("\n Ingrese el nuevo nombre para la campaña: ")
    campania.nombre = nuevo_nombre

    # Solicitar al usuario que ingrese un nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio: ")
    campania.anuncios[0].sub_tipo = nuevo_subtipo

except (LargoExcedidoError, SubTipoInvalidoError) as e:
    # Manejar las excepciones y escribir los mensajes en archivos de registro diferentes
    if isinstance(e, LargoExcedidoError):
        # Manejar la excepción de LargoExcedidoError y escribir el mensaje en un archivo de registro
        with open('dia13/prueba_modulo4/logs/largo_excedido_error.log', 'a+') as errorlargo:

            errorlargo.write(str(e) + '\n')
    elif isinstance(e, SubTipoInvalidoError):
        # Manejar la excepción de SubTipoInvalidoError y escribir el mensaje en un archivo de registro
        with open('dia13/prueba_modulo4/logs/subtipo_invalido_error.log', 'a+') as errorsubtipo:
            print("\n El subtipo no es válido:\n")
            errorsubtipo.write(str(e) + '\n')

print(campania)