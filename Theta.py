#Esta clase tendra como entrada una imagen en blanco y negro, la cual se podra filtrar respecto al angulo de orientacion. Para esto
#se debera definir cual es el valor del angulo de orientacion donde se realizara el filtrado y el delta que tendra este angulo de orientacion.

#Importacion de librerias

import cv2
import numpy as np
import os
import sys

#Creacion de la clase Theta
class Theta():


    #Creacion de metodo constructor donde se recibe la imagen en blanco y negro
    def __init__(self,image_gray):
        self.image_gray= image_gray

    #Creacion de metodo para establecer el valor de teta y delta de teta
    def set_theta(self,thetha,delta):
        self.theta=thetha #Declaracion de tetha para usar en la clase
        self.delta=delta #Declaracion de delta de tetha para usar en la clase

    #Creacion de metodo para filtrar la imagen a traves angulos de orientacion
    def filtering(self):
        #Se realiza la transformada de fourier a la imagen a blanco y negro
        image_gray_fft = np.fft.fft2(self.image_gray)
        #Se realiza el corrimiento de las frecuencias de la transformada de fourier
        image_gray_fft_shift = np.fft.fftshift(image_gray_fft)

        #Creacion de matriz para filtro
        filter = np.zeros_like(self.image_gray)

        #Creacion de matrices para filas y columnas de filtro
        num_rows, num_cols = (self.image_gray.shape[0], self.image_gray.shape[1])
        enum_rows = np.linspace(0, num_rows - 1, num_rows)
        enum_cols = np.linspace(0, num_cols - 1, num_cols)
        col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
        half_size = num_rows / 2   # Se asume que num_rows = num_columns

        #Se centran las matrices de filas y columnas
        x = col_iter - half_size
        y = row_iter - half_size

        # Se halla el angulo en grados con respecto a la vertical tanto para los cuadrantes superior e inferior
        area = (180 / np.pi) * (np.arctan2(x, y))
        area2 = ((180 / np.pi) * (np.arctan2(x, y * (-1))))

        # Se realiza una comparacion de cada angulo obtenido con el limite superior ingresado por el usuario (teta + delta de teta)
        mask_area1 = area < self.theta+self.delta
        mask_area11 = area2 > (self.theta+self.delta) * -1

        # Se realiza una comparacion de cada angulo obtenido con el limite inferior ingresado por el usuario (teta - delta de teta)
        mask_area2 = area > (self.theta-self.delta)
        mask_area22 = area2 < (self.theta-self.delta) * -1

        #Se realiza dos comparaciones AND, entre los resultados obtenidos para los cuadrantes superior, y, por otro lado para los del inferior
        mask_area = np.bitwise_and(mask_area1, mask_area2)
        mask_area3 = np.bitwise_and(mask_area11, mask_area22)

        #Luego se realiza una comparacion OR para tener la mascara del filtro completa y se asigna el valor de 1 a los valores true obtenidos del OR
        mask = np.bitwise_or(mask_area, mask_area3)
        filter[mask] = 1


        #Se aplica el filtro a la imagen en blanco y negro en fourier
        fft_filtered = image_gray_fft_shift * filter
        #Se realiza la inversa de fourier junto con el corrimiento nuevamente, y se normaliza la imagen filtrada
        image_filtered = np.fft.ifft2(np.fft.fftshift(fft_filtered))
        image_filtered = np.absolute(image_filtered)
        image_filtered /= np.max(image_filtered)

        return image_filtered



