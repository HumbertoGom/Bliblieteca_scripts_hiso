clear;clc;close

M1 = [3, 2; 1 -1]
y1= [7;-1]

M2 = [3,2;
      1,-1;
      4,1 ]
y2= [7;-1;6]


x1a = inv(M1) * y1
x1b = pinv(M1) * y1
x1c = linsolve(M1,-y1)
x1d = rref([M1,y1])
disp('invsera, pseudo-inversa, linsolve e rref nessa ordem')
disp('soluções para 1,',x1a ,x1b,x1c,x1d)



x2b = pinv(M2) * y2
x2c = linsolve(M2,-y2)
x2d = rref([M2,y2])
disp(' pseudo-inversa, linsolve e rref nessa ordem')
disp('soluções para 2' ,x2b,x2c,x2d)

