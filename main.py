# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
from colorImage import *

if __name__ == '__main__':
    # Solicitar ruta acceso
    path = input('Por favor ingrese la ruta de su imagen: ')
    # Solicitar nombre de la imagen
    image_name = input('Por favor ingrese el nombre de su imagen con su respectiva extensión: ')
    # Determinar la ruta de acceso a la imagen
    path_file = os.path.join(path, image_name)
    # Crear imagen de interes
    image = colorImage(path_file)
    # Visualizar imagen
    cv2.imshow('Imagen original', image.image)
    cv2.waitKey(5000)
    # Desplegar ancho y alto de la imagen seleccionada
    image.displayProperties()
    # Convertir imagen de interes en escala de grises
    gray=image.makeGray()
    # Visualizar imagen en escala de grises
    cv2.imshow('Imagen gris', gray)
    cv2.waitKey(5000)
    # Forzar conversión de tono a rojo
    color = 'Red'
    colorpngv=image.colorizeRGB(color)
    # Visualizar imagen rojiza
    cv2.imshow('Imagen rojiza', colorpngv)
    cv2.waitKey(5000)
    # Modificar HSV para retornar a RGB
    colorhuev = image.makeHue()
    # Visualizar imagen hue
    cv2.imshow('Imagen HUE', colorhuev)
    cv2.waitKey(5000)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
