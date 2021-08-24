
#Se importan las librerias a utilizar junto con la clase Theta creada

import cv2
import numpy as np
import os
import sys
from Theta import Theta as Th


#Creacion de funcion para obtener el filtro de una imagen para los grado de orientacion de: 0, 45, 90 y 135.
def banco_filtros_direcc(image_gray):


    #Filtrado con orientacion de 0 grados
    imagen0 = Th(image_gray)
    imagen0.set_theta(0, 5)
    imagen0_F = imagen0.filtering()

    # Filtrado con orientacion de 45 grados
    imagen45= Th(image_gray)
    imagen45.set_theta(45, 5)
    imagen45_F = imagen45.filtering()

    # Filtrado con orientacion de 90 grados
    imagen90= Th(image_gray)
    imagen90.set_theta(90, 5)
    imagen90_F = imagen90.filtering()

    # Filtrado con orientacion de 135 grados
    imagen135= Th(image_gray)
    imagen135.set_theta(135, 5)
    imagen135_F = imagen135.filtering()

    #Retorno de imagenes filtradas
    return(imagen0_F, imagen45_F, imagen90_F, imagen135_F)



#Definicion de funcion main
if __name__ == '__main__':
    #Se toman los parametros de la ruta donde se encuentra la imagen y el nombre de la imagen
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)

    #Lectura de la imagen ingresada y se convierte a blanco y negro
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Uso de la funcion para obtener los diferentes filtrados respecto al grado de orientacion
    imagen0,imagen45,imagen90,imagen135= banco_filtros_direcc(image_gray)

    #Imagen obtenido del promedio de las imagenes filtradas
    imagen_resultante= (imagen0+imagen45+imagen90+imagen135)/4

    #Mostrado en pantalla de la imagen original junto con las imagenes filtradas y la imagen promedio resultante de estas.
    cv2.imshow("Imagen original", image_gray)
    cv2.imshow("Imagen filtro 0 grados", imagen0)
    cv2.imshow("Imagen filtro 45 grados",imagen45)
    cv2.imshow("Imagen filtro 90 grados",imagen90)
    cv2.imshow("Imagen filtro 135 grados",imagen135)
    cv2.imshow("Imagen resultante del promedio", imagen_resultante)
    cv2.waitKey(0)

