clear;clc;close

//EXEMPLO 2 - INFINTAS SOLUÇÕES

u=[2,3,-1,4,5]'
v=[-1,0,1,2,3]'
w=[0,2,1,4,3]'


A= [u ,v ,u-v ,w ,u-w ]
y= 2*u + v - w

disp(A)

//Matriz reduzida
Mred = rref([A,y])
disp(Mred)



//   1.   0.   1.   0.   1.   2.
//   0.   1.  -1.   0.   0.   1.
//  0.   0.   0.   1.  -1.  -1.
// 0.   0.   0.   0.   0.   0. 
// 0.   0.   0.   0.   0.   0.


//colunas 1 e 2 são linearmente dependentes
//variaveis 3 e 5 são dependente lineares
//rref pula a terceira,mas conseugiu ajustar x4, x4 é LI tambem
//coluna 6 do Y é linearmente dependete, mas não importa
// onde esta 


//I(3x3) . (x1;x2;x4) +  (1;-1;0)x3 +(1;0;-1)x5 = (2;1;-1)
//simplifcicar cortando identidade


