import numpy as np
import scipy
from scipy import signal
import scipy.fftpack
import cv2
import matplotlib.pyplot as plt
def dct2d(input):
    return scipy.fftpack.dct(scipy.fftpack.dct(input, axis=0, norm='ortho' ),axis=1, norm='ortho' )

def dct2d_inv(input):
    return scipy.fftpack.idct(scipy.fftpack.idct(input, axis=0 , norm='ortho'),axis=1 ,norm='ortho')

img_entrada = cv2.imread('imagen1.jpg',cv2.IMREAD_GRAYSCALE)

A=np.zeros((64,64))
F=np.zeros((64,64,8,8))
for m in range(64):
    for n in range(64):
        block = img_entrada[m*8:m*8+8,n*8:n*8+8]
        dct2d_block=dct2d(block)
        A[m,n]=dct2d_block[0,0]
        F[m,n,:]=dct2d_block

U,S,Vt=np.linalg.svd(A,False)

#marca de agua
W = cv2.imread('marca.jpg',cv2.IMREAD_GRAYSCALE)
alpha=0.1
SaW = np.diag(S) + alpha*W

U_1,S_1,Vt_1=np.linalg.svd(SaW,False)

Ah= U @ np.diag(S_1) @ Vt

#imagen con marca de agua incrustada
Iw= np.zeros(img_entrada.shape)

for m in range(64):
    for n in range(64):
        #modifica la componente DC de transformada original 
        F[m,n,0,0] = Ah[m,n]
        #calcula la transformada inversa del bloque modificado
        dct2d_inv_block=dct2d_inv(F[m,n,:])
        #guarda el bloque nuevo en Iw
        Iw[m*8:m*8+8,n*8:n*8+8] = dct2d_inv_block
#recortar valores
Iw[Iw>255]=255
Iw[Iw<0]=0
Iw= Iw.astype(np.uint8)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.subplot(2,2,1)
plt.imshow(img_entrada,cmap='gray')
plt.title('I (original)')

plt.subplot(2,2,2)
plt.imshow(W,cmap='gray')
plt.title('W (marca de agua)')

plt.subplot(2,2,3)
plt.imshow(Iw,cmap='gray')
plt.title('Iw (marca incrustada)')
plt.show()




