import numpy as np

def escalonar_matriz(matriz):
    """
    Escalona a matriz para a forma de escada, zerando os elementos abaixo de cada pivô.
    """
    matriz = matriz.astype(float)  # Garantir que os cálculos sejam com floats
    linhas, colunas = matriz.shape
    
    for i in range(min(linhas, colunas - 1)):  # Evita a última coluna (termos independentes)
        # Escolher o pivô
        if matriz[i, i] == 0:
            for k in range(i + 1, linhas):
                if matriz[k, i] != 0:
                    matriz[[i, k]] = matriz[[k, i]]  # Troca as linhas
                    break
        
        if matriz[i, i] == 0:
            continue  # Se a coluna for toda zero, pula
        
        # Zerar os elementos abaixo do pivô
        for j in range(i + 1, linhas):
            fator = matriz[j, i] / matriz[i, i]
            matriz[j] -= fator * matriz[i]
    
    return matriz

# Exemplo de uso
matriz = np.array([
    [1, 1, 1, 1],
    [2, -1, 3, 0],
    [-1, 1, -5, 2]
], dtype=float)

matriz_escalonada = escalonar_matriz(matriz)
print("Matriz escalonada:")
print(matriz_escalonada)

#print('esse é o numero de linhas certo?',matriz_escalonada.shape[0])
posto_ampliada = np.linalg.matrix_rank(matriz_escalonada)

matriz_coeficiente = matriz_escalonada[:,0:-1]
print('\nmatriz coeficiente\n', matriz_coeficiente)

posto_coeficiente = np.linalg.matrix_rank(matriz_coeficiente)

print(f'Posto ampliada = {posto_ampliada}\n e posto coefiente = {posto_coeficiente}')
if posto_coeficiente == posto_ampliada:
    if posto_ampliada == (matriz_escalonada.shape[1]-1):
        print('é um sitema possível determinado')
    else:
        print('é um sistema possível indeterminado ')
else:
    print('sistema impossível')