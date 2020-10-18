clc; clear; close all
pkg load image
pkg load video
imagen=imread('barbara.jpg');

imagen_filtrada=mediana(imagen);
imshow(imagen_filtrada)