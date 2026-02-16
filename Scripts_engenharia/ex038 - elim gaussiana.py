import numpy as np

X= np.array([[1,3,4],
            [5,7,8],
            [9,11,12]])

Y= np.array([[3],[2],[1]])

Matriz_ampliada = np.hstack((X,Y))
print(f'Matirz ampliada{Matriz_ampliada} \n'
)

res= np.linalg.lstsq(X,Y,rcond=None)[0]

print(res)