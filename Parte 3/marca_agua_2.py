import numpy as np
import scipy
from scipy import signal
import scipy.fftpack
import cv2
import matplotlib.pyplot as plt

import scipy.io as sio

def dct2d(input):
    return scipy.fftpack.dct(scipy.fftpack.dct(input, axis=0, norm='ortho' ),axis=1, norm='ortho' )

def dct2d_inv(input):
    return scipy.fftpack.idct(scipy.fftpack.idct(input, axis=0 , norm='ortho'),axis=1 ,norm='ortho')

#ir a octave load 'V1.mat'
# cambiar de formato a v7
#save -v7 V1.mat V1
U1=sio.loadmat('U1.mat')['U1']
V1=sio.loadmat('V1.mat')['V1']

Iw= cv2.imread('imagen2.jpg',cv2.IMREAD_GRAYSCALE)
I= cv2.imread('imagen3.jpg',cv2.IMREAD_GRAYSCALE)
A=np.zeros((256,256))
for m in range(256):
    for n in range(256):
        block= I[m*4:m*4+4,n*4:n*4+4]
        block_dct=dct2d(block)
        A[m,n]=block[0,0]

U, S, Vt = np.linalg.svd(A,False)


A_star=np.zeros((256,256))
for m in range(256):
    for n in range(256):
        block= Iw[m*4:m*4+4,n*4:n*4+4]
        block_dct=dct2d(block)
        A_star[m,n]=block[0,0]

U_s, S1_s, Vt_s = np.linalg.svd(A_star,False)

D_star = U1 @ np.diag(S1_s) @ V1.transpose()

W_star = (1/0.1)*(D_star-np.diag(S))

W_star[W_star>255]=255
W_star[W_star<0]=0

W_star=W_star.astype(np.uint8)
plt.subplot(2,2,1)
plt.imshow(Iw,cmap='gray')
plt.title("imagen con marca")

plt.subplot(2,2,2)
plt.imshow(W_star,cmap='gray')
plt.title('marca extraida')

plt.show()
