import numpy as np

#A=np.matrix('1,1,1,1 ; 2,-1,3,0 ; -1,1,-5,2') objeto matrix não é recomendado,vou usar array mesmo.
A=np.array([[1,1,1,1],[2,-1,3,0],[-1,1,-5,2]],dtype= float)

print (A)

#Aquadrada= np.matrix('1,1,1 ; 2,-1,3 ; -1,1,-5')
#transposta = Aquadrada.T
#print (transposta)

print(A.shape)
linhas = A.shape[0]

colunas =A.shape[1]

print('')
print(f'a matriz tem {linhas} linhas e {colunas} colunas') 



print('')
indice_pivot = 0
#esse laço torna as diagonais em 1
for i in range(linhas):

    print (f'o index do pivot atual é {indice_pivot}')
    valor_pivot = A.item(indice_pivot)
    print(f'o item correspodente ao pivot atual é {A.item(indice_pivot)}')
    print(A[i])

    for j in range(colunas):
        j=j 
        A[i][j] = float(A[i][j])
        A[i][j] = (A[i][j]) / valor_pivot
    print(f'a linha agora é {A[i]}' )
    indice_pivot +=colunas + 1

print(A)
print('')


indice_pivot = 0
multiplo= 0

for i2 in range(linhas):
    if i2 == 1:
        continue
    pivot = A.item(indice_pivot)
    
    multiplo = A.item(i2*colunas)/pivot
    for j2 in range(colunas):
        A[i2][j2] = A[i2][j2] + multiplo * pivot
        print(A)
    indice_pivot +=colunas + 1
print(A)
