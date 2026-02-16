import numpy as np

# Definindo as matrizes
#A = np.array([[10, 20,30], [40, 50,60]])
#B= np.array([[10, 20,30], [40, 50,60]])

# Multiplicação de matrizes
#C = np.dot(A, B)


#calculando transpota

#matriz_tranposta = A.T 
#print(matriz_tranposta)


B=np.array([[10, 20,30], [40, 50,60]])


matriz = np.array([[5, 12, 7], [3, 8, 10], [-4, -6, -9]])

#valor máximo e min

maximodamatriz = np.max(matriz)
print(f'o valor máximo da matriz é {maximodamatriz}')
minimodamatriz = np.min(matriz)
print(f'o valor mínimo da matriz é {minimodamatriz}')



# Obtendo os índices do valor máximo e mínimo
indice_maximo = np.unravel_index(np.argmax(matriz), matriz.shape)
indice_minimo = np.unravel_index(np.argmin(matriz), matriz.shape)


print("Matriz:")
print(matriz)
print(f"Índice do valor máximo: {indice_maximo}")
print(f"Índice do valor mínimo: {indice_minimo}")



#absoluto da matriz

matriz_absoluta = np.abs(matriz)

print("Matriz original:")
print(matriz)
print("Matriz com valores absolutos:")
print(matriz_absoluta)
