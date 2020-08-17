import cv2
import os

class colorImage:

    def __init__(self, path_file): # Ruta imagen
        self.image = cv2.imread(path_file)

    # Visualiza en pantalla (via print) el ancho y alto de la imagen
    def displayProperties (self): # Propiedades display
        self.height = self.image.shape[0] # image.shape indica la altura en la posición 0
        self.width = self.image.shape[1] # image.shape indica la altura en la posición 1
        print('Alto: ', self.height, '\nAncho: ', self.width)

    # Devuelve una versión en grises de la imagen
    def makeGray(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) # Convertir imagen original en escala grises
        return gray # Retornar imagen en escala grises

    # Recibe un string correspondiente a un canal de color y regresa una imagen colorizada
    def colorizeRGB(self, color):
        image2=self.image.copy() # Generar copia imagen original
        if color == 'Green':
            image2[:,:,0] = 0 # Componente azul a cero
            image2[:,:,2] = 0 # Componente rojo a cero
            return image2
        elif color == 'Red':
            image2[:,:,1] = 0 # Componente verde a cero
            image2[:,:,0] = 0 # Componente azul a cero
            return image2
        elif color == 'Blue':
            image2[:,:,1] = 0 # Componente verde a cero
            image2[:,:,2] = 0 # Componente rojo a cero
            return image2
        else:
            # Caso en donde se ingresa un string invalido
            print('Por favor ingrese un término valido')

    # Devuelve una imagen que resalta los tonos (Hue) de la imagen original
    def makeHue(self):
        hue = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) # RGB a HSV
        hue[:, :, 1] = 255 # Componente S a 255
        hue[:, :, 2] = 255 # Componente V a 255
        image = cv2.cvtColor(hue, cv2.COLOR_HSV2RGB) # HSV a RGB
        return image # Devolver imagen resultante

        # Press the green button in the gutter to run the script.