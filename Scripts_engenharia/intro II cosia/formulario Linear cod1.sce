u = [1;2;0;4]
  v = [-3;2;1;0]
  w = [4;3;5;6]
A = [u,  v,  u-v,  w,  u+2*w]
y = [2*u-v+3*w]

//disp('Usando Inversa ', inv(A)*y) 
//inv retorna error:"Square matrix expected. Please use pinv() otherwise."
disp('Usando Pseudo-Inversa ', pinv(A)*y)
disp('Usando rref ', rref([A,y]))
disp('Usando Linsolve ', linsolve(A,-y))

