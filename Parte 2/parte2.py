import cv2
from os import listdir
from os.path import isfile, join
import numpy as np

imagen_a_limpiar=cv2.imread("limpiar.jpg",cv2.IMREAD_GRAYSCALE)
shape = imagen_a_limpiar.shape
rows=shape[0]
cols=shape[1]

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
   
u_b,s_b,vh_b=np.linalg.svd(B_ruido,False)
eps=np.finfo(s_b.dtype).eps #lo que es considerado 0 por python
rango_b=len(s_b[s_b>eps])
Vs=vh_b.transpose()[:,0:rango_b]
P= C_orig@Vs@Vs.transpose()
B_pinv= vh_b.transpose() @ np.linalg.inv(np.diag(s_b)) @ u_b.transpose() #B†

u_p,s_p,vh_p=np.linalg.svd(P,False)


for r in rangos:
    Pr= u_p[:,0:r] @np.diag(s_p[0:r]) @ vh_p.transpose()[:,0:r].transpose()
    Zt=Pr@B_pinv
    reconst=np.dot(Zt,imagen_a_limpiar.reshape(rows*cols))

    reconst=reconst.reshape(rows,cols)
    reconst[reconst<0]=0
    reconst[reconst>255]=255
    reconst=reconst.astype(np.uint8) 
    cv2.imwrite('limpia_r'+str(r)+'.jpg',reconst)