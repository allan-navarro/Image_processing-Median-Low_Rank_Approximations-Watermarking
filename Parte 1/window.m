%esta funcion calcula la mediana del pixel ubicado en la posicion "index"
%llamar con  Res=arrayfun (@(o) window(A,o),[1 2 3;4 5 6;7 8 9]) ;
%A = canal de entrada
%w = mediana del pixel con una ventana de 3
function [r,g,b] = window(A,index)
  row = idivide(index,columns(A),'floor');
  if row!= index/columns(A) 
    row=row+1;
  end
  col = mod(index-1,columns(A))+1;
  
  start_col=max(1,col-1);
  end_col= min(columns(A),col+1);
  
  start_row=max(1,row-1);
  end_row=min(rows(A),row+1);
  tic
  r= median(median(A(start_row:end_row,start_col:end_col,1)));
  g= median(median(A(start_row:end_row,start_col:end_col,2)));
  b= median(median(A(start_row:end_row,start_col:end_col,3)));
  toc
endfunction