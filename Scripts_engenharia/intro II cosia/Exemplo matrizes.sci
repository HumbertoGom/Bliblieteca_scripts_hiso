clear;clc;close

// Escrita de matriz
//M = [10, 20, 30;
//     40, 50, 60]

// // Vetor linha
//v = [10, 20, 30]
// Vetor coluna 
//w = [100; 200; 300]


// Mudando o elemento (1,1) da matriz M
//M(1,1) = 600

// Imprima a 1a coluna
//disp(M(:,1))

//disp ('-----')

// Imprima a 2a linha
//disp (M(2,:))

// Criando matrizes de
//A = zeros(5,4) // zeros
//B = ones (5,4) // uns
//C = rand(5,4)  // aleatórios
//D = eye(5,4)   // identidade

// Exemplo criar uma matriz M de 5x3
//M = zeros(5,3)
//for i =1:5
//    for j= 1:3
//        M(i,j) = i +2*j
//    end
//end

// Multiplicação matricial
//A = [10,20,30;
//     40,50,60]
//v = [15;12;16]
//disp(A*v) // multiplicação certa
//// disp(v*A) // não tem produto, vai dar erro



//// Exercício matriz transposta
//disp(A') 


// Exercício máximo\mínimo
//B = [10, 50, 70;
//     90, 120, -8]
//[vmax,pmax] =max(B)
//[vmin,pmin] = min(B)


// Absoluto da matriz
//K = abs([-5,6,7;-9,12,-15])


// Eliminação Gaussiana
//A = [2, 5, -5;
//     -1, 3, 1;
//     0, 2, -4]

// y = [6; -4; 2]
 // M = [A,y] // matriz extendida

//for i = 1:n
//    pivo = M (i,j)
//    M (i,:) = M (i,:)/pivo
//    for = [1:i-1,i+1:n]
//        M (j,:) = M (j,:)- M(I,:)*M(j,i)
//    end    
//end

// pivo = M(1,1) // para arrumar a 1a coluna
// M(1,:) = M(1,:)/pivo
// M (2,:) = M(2,:) - M(1,:)*M(2,1)
// M(3,:) = M(3,:) - M(1,:)*M(3,1)

// pivo=M(2,2) // para arrumar a 2a coluna
// M(2,:)=M(2,:)/pivo
//M(1,:)=M(1,:)-M(2,:)*M(1,2)
//M(3,:) = M(3,:) - M(2,:)*M(3,2) 

// pivo=M(3,3)
// M(3,:)=M(3,:)/pivo
// M(1,:)=M(1,:)-M(3,:)*M(1,3)
// M(2,:)=M(2,:)-M(3,:)*M(2,3)

// 3 tipos de problemas:
// 1: solução única [A].[x^seta]=[y^seta]
// 2: infinitas soluções 
// 3 sem solução 

// Posto (Matriz) = número de linhas e colunas linearmente independentes entre si 

// TEOREMA DA ÁLGEBRA SOBRE MATRIZES: 

// (número de linas LI) = (número de colunas LI) = POSTO (MATRIZ)

// SISTEMA:
// a11x1 + a12x2+...+a1nxm = y1
// a21x1 + a22x2+..+a2nxm = y2
// ...
// an1x1 + an2x2 + ... anmxm = yn

// x1*(a11;a21;...;an1) + x2*(a12;a22;...an2)+ ...+ xm(a1m;a2m;...;anm)=(y1;y2;...yn)

// (a11;a21;...;an1) : 1º vetor coluna de a
//(a12;a22;...an2) : 2º vetor coluna de a
// (a1m;a2m;...;anm) : n vetor coluna de a 
// (y1;y2;...yn) : vetor y

//A equação acima diz que: O Y deve ser uma combinação linear dos vetores colunas de a. Se não tiver essa combinação, o sistema não tem solução.

// y vetor é combinação dos vetores colunas da matriz A.

// y vetor pertence span{a1 vetor, a2 vetor, ...} -> span ... = espaço vetorial

// A*X VETOR = Y VETOR
// posto() -> (nº de linhas e colunas LI) == posto (A Y)(nº de linhas e colunas LI) -> se o caso satisfazer, então há solução.


// considere a matriz
A = [3, 2 ; 1, -1]
xconhecido = [1;2]
y = A * xconhecido

// posto da matriz A
disp('posto de A',rank(A))
//posto da matriz estendida 
disp('posto de M',rank([A,y]))

// para haver solução única, as colucas da matriz A devem ser todas LI. Logo, posta (A)= nº de colunas de A.


// aumentando 'artificialmente o sistema'
A2 = [A(1,:)
      A(2,:)
      A(1,:)+A(2,:)]
      
y2 = [y(1)
      y(2)
      y(1)+y(2)]
     
// posto da matriz A
disp('posto de A2',rank(A2))
//posto da matriz estendida 
disp('posto de M2',rank([A2,y2]))


// aumentando criando uma variável
A3 = [A2(:,1), A2(:,2), A2(:,1)+A2(:,2)]
y3 = y2 
     
// posto da matriz A
disp('posto de A3',rank(A3))
//posto da matriz estendida 
disp('posto de M3',rank([A3,y3]))


function saida =diagnostico(A,y)
    // pergunta se há solução
    if rank (A)==rank([A,y]) then
        // pergunta se eh unica
        if rank(A)==size(A,2) then
            saida = 'sol unica'
        else
            saida = 'inf sol'
        end
    else
        saida = 'sem sol'
    end
// size(A,2) -> Nº DE COLUNAS DE A.
endfunction
saida1 = diagnostico(A,y)
disp('sistema 1',saida1)
            
saida2 = diagnostico(A2,y2)
disp('sistema 2',saida2)

saida3 = diagnostico(A3,y3)
disp('sistema 3',saida3)

   

x = inv(A)*y
//funciona se o sistema for quadrado e a inversa existir.

x = pinv(A)*y 
ou
x = linsolve(A,-y)
ou
disp(rref([A,y]))
//vai funcionar se o sistema não for quadrado.







