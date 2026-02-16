M = [[10,20, 30],
     [40,50,60]]




print(M[1][1])

v=[[10, 20 ,30]]

w= [[100],[200],[300]]

import random

A= []
lista_temp_de_soma=[]
k=0

for i in range(5):

     i+=1
     for j in range(3):
        j+=1
        k+=i+2*j
        print(i,j)
        lista_temp_de_soma.append(k)
     A.append(lista_temp_de_soma)
     lista_temp_de_soma = []

print(lista_temp_de_soma)
print(A)