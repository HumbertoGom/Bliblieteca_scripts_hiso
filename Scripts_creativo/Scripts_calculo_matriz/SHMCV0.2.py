#SHMC V0.2
import numpy as np 

#Matriz = np.full((3,3),'-')
#print (Matriz)
Matriz = []

def criar_matriz(l,c):
    l=input('Digite o Número de Linhas ')
    c=input('Digite o Número de Colunas ')
    if l.isdigit() and c.isdigit():
        l = int(l)
        c = int(c)
    else:
        print('Por favor digite um número válido ')
    Matriz = np.full((l,c),'-')
    print(Matriz)
    return Matriz


Matriz= criar_matriz(1,1)
print( Matriz.size)

k=0
l=0
j=0

for i in Matriz:
    for k in Matriz:
        entrada = input('Digite um valor')
        if entrada.isdigit:
            entrada = int(entrada)
        else:
            continue
        if l > Matriz.shape[1]:
            break
        Matriz[j,l] = entrada
        print(Matriz)
        l+=1
    j+=1
    if j > Matriz.shape[0]:
        break


