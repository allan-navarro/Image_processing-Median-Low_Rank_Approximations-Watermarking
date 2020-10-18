function Y = mediana(A)

[m,n,canales]=size(A); %dimensiones de la imagen con ruido
imagen_filtrada=zeros(m,n,canales); %imagen filtrada inicializada en ceros

% primer intento, loop, muy lento
#{
tic
for col=1:n
  start_col=max(1,col-1);
  end_col= min(n,col+1);
  strip=imagen(:,start_col:end_col,:);
  for row =1:m
      start_row=max(1,row-1);
      end_row=min(m),row+1);
      r= median(median(strip(start_row:end_row,:,1)));
      g= median(median(strip(start_row:end_row,:,2)));
      b= median(median(strip(start_row:end_row,:,3)));
      imagen_filtrada(row,col,1)=r;
      imagen_filtrada(row,col,2)=g;
      imagen_filtrada(row,col,3)=b;    
  end
end
toc
#}

%vectorizado
# {
%itera los canales
for canal=1:canales
  image_vec=A(:,:,canal)(:); %extrae el canal y lo vectoriza

%se ponen los 9 pixeles de la ventana en filas
  row_median = [image_vec circshift(image_vec,-1) circshift(image_vec,-2) \
             circshift(image_vec,-m) circshift(image_vec,-m-1) circshift(image_vec,-m-2) \
             circshift(image_vec,-2*m) circshift(image_vec,-2*m-1) circshift(image_vec,-2*m-2) ];
             
  med=median(row_median,2); %calcula la mediana por filas
  imagen_filtrada(:,:,canal)=reshape(med,m,n); %convierte  de vector a matriz
end

#}

imagen_filtrada=uint8(imagen_filtrada);
Y=imagen_filtrada;
endfunction
