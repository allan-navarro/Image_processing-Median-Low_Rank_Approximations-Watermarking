import cv2
from os import listdir
from os.path import isfile, join
import numpy as np

imagen_a_limpiar=cv2.imread("limpiar.jpg",cv2.IMREAD_GRAYSCALE)
shape = imagen_a_limpiar.shape
rows=shape[0]
cols=shape[1]
print(shape)
rangos=[40,120, 220, 300, 380, 416]

imgs_ruido= [join('.','ruido',f) for f in listdir('ruido') if isfile(join('ruido',f))] #lista con el nombre de las imagenes originales
imgs_orig= [join('.','original',f) for f in listdir('original') if isfile(join('original',f))] #lista con el nombre de las imagenes con ruido

#verifica que el numero de imagenes sean iguales en ambos directorios
if len(imgs_ruido) != len(imgs_orig):
    print('no coincide la cantidad de imagenes original con las imagenes con ruido')
    exit(-1)


#carga las imagenes a una matriz
#C: imagenes originales
C_orig=np.zeros((rows*cols,len(imgs_orig)))
#B: imagenes con ruido
B_ruido=np.zeros((rows*cols,len(imgs_ruido)))
for index in range(len(imgs_orig)):
    #trae los nombres de los archivos de la lista
    img_ruido_path=imgs_ruido[index]
    img_orig_path=imgs_orig[index]

    #carga las imagenes y las vectoriza
    B_ruido[:,index]=cv2.imread(img_ruido_path,cv2.IMREAD_GRAYSCALE).reshape(rows*cols)
    C_orig[:,index]=cv2.imread(img_orig_path,cv2.IMREAD_GRAYSCALE).reshape(rows*cols)
   



for r in rangos:
    print(r)


cv2.imshow("img",imagen_a_limpiar)
cv2.waitKey(0)