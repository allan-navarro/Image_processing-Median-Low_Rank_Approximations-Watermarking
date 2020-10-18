clc; clear; close all
pkg load image
pkg load video
%cargar el video
video_con_ruido = VideoReader('video_con_ruido.mp4');
%numero de frames
frames=video_con_ruido.NumberOfFrames;

%crear el video nuevo 
video_filtrado = VideoWriter('video_sin_ruido.mp4');

%leer frame por frame
for f=1:frames
  frame = readFrame(video_con_ruido);
  frame = mediana(frame);
  %guardar frame filtrado en el video nuevo
  writeVideo(video_filtrado,frame);
endfor
%cerrar archivos de video
close(video_filtrado);
close(video_con_ruido);
