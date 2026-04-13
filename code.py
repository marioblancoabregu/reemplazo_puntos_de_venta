##EJECUTADO VIA GOOGLE COLABS##

from google.colab import files

def limpiar_archivo(contenido):
    reemplazos = {
        'TIENDA_A, UBICACION': 'TIENDA_A UBICACION',
        'TIENDA_B, UBICACION': 'TIENDA_B UBICACION',
        'TIENDA_C, UBICACION': 'TIENDA_C UBICACION'
    }

    for original, nuevo in reemplazos.items():
        contenido = contenido.replace(original, nuevo)

    return contenido

try:
    #Subir archivo CSV:
    uploaded = files.upload()
    ruta_original = list(uploaded.keys())[0]

    #Leer archivo y encontrar reeemplazos:
    with open(ruta_original, 'r', encoding='latin-1') as file:
        contenido = file.read()

    #Procesar cambios:
    contenido_limpio = limpiar_archivo(contenido)

    #Guardar archivo:
    ruta_editado = "output_limpio.csv"
    with open(ruta_editado, 'w', encoding='latin-1') as file:
        file.write(contenido_limpio)

    #Descargar archivo en local:
    files.download(ruta_editado)

    print("Archivo procesado correctamente")

except Exception as e:
    print(f"Error al procesar el archivo: {e}")
