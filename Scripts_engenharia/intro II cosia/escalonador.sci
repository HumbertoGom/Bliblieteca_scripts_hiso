clear;clc;close

A = input("Digite uma matriz 3x3 qualquer: ")
y = input("Digite uma matriz 3x1 qualquer: ")

M = [A,y]

[n,m] = size(M)
// n=  LINHAS
// m= COLUNAS

for i = 1:n
    pivo = M(i,i)
    M(i,:) = M(i,:)/pivo
    for j = 1:n
        if j ~= i
            M(j,:) = M(j,:) - M(j,i)*M(i,:)
        end
    end
end

disp("Sistema resolvido: ")
disp(M)