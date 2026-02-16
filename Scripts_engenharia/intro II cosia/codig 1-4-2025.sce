clear;clc;close

A=[3,2
    1,-1]
    
Xconhecido = [1;2]

y = A * Xconhecido

disp(y)

// posto de A

disp('posto de A', rank(A))

// posto da matriz extendida

disp('posto de M ' ,rank([A,y]))

//para haver solução única,as colunas devem ser todas LI(linearmente independentes)

//aumentando aritcificialidade do sistema

A2 = [A(1,:)
A(2,:)
A(1,:) + A(2,:)]

Y2= [y(1)
y(2)
y(1)+y(2)]

disp('posto de A2',rank(A2))

disp('posto de y2',rank([A2,Y2]))


//aumentando criando variável

//Criou uma terceria colunas somando as outras
A3 = [A2(:,1), A2(:,2), A2(:,1)+ A2(:,2)]
Y3= Y2

disp('posto de A3 ',rank(A3))
disp('posto da extendida' , rank([A3,Y3]))



function saida = diagnostico(A,y)
//    pergunta se ha solção
    if rank(A) == rank([A,y]) then
    // se é unica
        if rank(A) == size(A,2) then
        // se o posto é igual ao numero de colunas
            saida  = 'sol única'  
        else
            saida = 'inf soluções'
        end
    else
        saida = 'sem sol'
    end
    disp(saida)
endfunction

diagnostico(A,y)
diagnostico(A2,Y2)
diagnostico(A3,Y3)
