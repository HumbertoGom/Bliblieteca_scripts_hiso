clear;clc;close

A=[1,2,0;
  -1,3,2;
   4,1,-3]

ya=[1;-3;2]

//A_ampliada = (rref([A,ya]))
//A_coeficiente = A_ampliada(:,1:3);
//n_var_A = size(A,2)

//isso foi meu teste do algoritmo
//if rank(A_ampliada) == rank(A_coeficiente) then
//    disp('sistema possivel')
  //  if  rank(A_ampliada) == n_var_A then
   //     disp('sistema possivel determinado')
   // else
      //  disp('sistema possivel indeterminado(infinitas soluçoes)')
    //    disp(pinv(A)*ya)
  //  end
//else
//    disp('sistema impossível')
//    disp(pinv(A)*ya)
//end

//isso é minha função
function[solucao] = sistema_lin(A,y) 
    A_ampliada = (rref([A,y]))
    A_coeficiente = A_ampliada(:,1:3);
    n_var_A = size(A,2)   
    if rank(A_ampliada) == rank(A_coeficiente) then
        disp('sistema possivel')
        if  rank(A_ampliada) == n_var_A then
            disp('sistema possivel determinado')
        else
            disp('sistema possivel indeterminado(infinitas soluçoes)')
            disp(pinv(A)*y)
        end
    else
        disp('sistema impossível')
        disp(pinv(A)*y)
    end
    solucao = pinv(A)*y
    disp (solucao)
endfunction

sistema_lin(A,ya)



disp('item B')
B=[1,2,0;
-1,3,2
4,1,-3;
5,3,-3]

yb= [1;-3;2;3]

sistema_lin(B,yb)

C=[1,2,0,1;
-1,3,2,-4;
4,1,-3,2;
5,3,-3,3
]

yc=[-1;-3;2;3]

disp('item C')
sistema_lin(C,yc)


D=[1,2,0;
-1,3,2;
4,1,-3;
5,3,-3]

yd=[1;-3;2.5;3.2]

disp('item D')
sistema_lin(D,yd)



