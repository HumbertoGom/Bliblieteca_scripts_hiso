import numpy as np

while True:
    linhas = input('digite o número de linhas ')
    colunas = input(' digite o número de colunas ')
    try:
        linhas = int(linhas)
        colunas = int(colunas)
    except ValueError:
        print('digite apenas inteiros como linhas e colunas ')
        continue
    except:
        print('erro desconhecido')
        continue
    Matriz = []
    lista_provisoria = []
    for i in range(linhas):
        for j in range(colunas):
            lista_provisoria.append('-')
        print(lista_provisoria)
        Matriz += lista_provisoria
        lista_provisoria = []
    i=0
    j=0
    for i in range(linhas):
        for j in range(colunas):
            print(Matriz)
            entrada = input('Digite o próximo número da matriz, [R] para recomeçar')
            if entrada == 'R':
                i = 0
                j = 0
                continue
            try:
                entrada = float(entrada)
            except ValueError:
                print(' por favor digte um valor numerico ')
                i = 0 
                j = 0
                continue
            Matriz.insert(entrada,(i+j))

    Matriz = np.append(Matriz)