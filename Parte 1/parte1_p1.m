clc; clear; close all
pkg load image
pkg load video
imagen=imread('barbara.jpg');

[m,n,c]=size(imagen);

%crea una matrix de 1 a m*n que representa el indice de cada pixel de 
%la imagen de entrada
tic
pixel_index=reshape([1:m*n],n,[])';
toc
%aplica la funcion window a la matriz pixel_index
[r,g,b]=arrayfun (@(o) window(imagen,o),pixel_index);
imagen_filtrada=zeros(m,n,c);
imagen_filtrada(:,:,1)=r;
imagen_filtrada(:,:,2)=g;
imagen_filtrada(:,:,3)=b;
imagen_filtrada(1:5,1:5)
imagen_filtrada=uint8(imagen_filtrada);

imshow(imagen_filtrada)