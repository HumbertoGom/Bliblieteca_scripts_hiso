import numpy as np
from scipy import optimize
from itertools import product


# --------------------
# Dados do problema
# --------------------
#0 - fazenda 1, 1- Fazenda 2, 2 - Fazenda 3
F = [0,1,2]
# 0- Milho, 1- arroz, 2- Feijão
C = [0,1,2]

Af = [400,650,350] #area disponivel
Wf = [1800,2200,950] #água disponível

Ac = [660,880,400] #área máxima
Kc = [5.5,4,3.5]   #Consumo de água
Lc = [5000,4000,1800] #Lucro de cada cultura

# variáveis iniciais
Scf = np.array([
   [101,102,103],
   [101,300,103],
   [101,102,103]
])

Ycf = np.array([
   [True,False,True],
   [True,False,True],
   [True,False,True]
])


# --------------------
# Função objetivo
# --------------------
def Fobj(x):
    # primeiros 9 elementos = Ycf, últimos 9 = Scf
    Ycf_flat = x[:9]
    Scf_flat = x[9:]
    Ycf = Ycf_flat.reshape(3,3)
    Scf = Scf_flat.reshape(3,3)

    # lucro bruto
    ganho = (Lc * Scf).sum()
    # custo fixo por plantação existente
    custo = 5000 * Ycf.sum()

    lucro = ganho - custo
    
    return -lucro

comb_binars =np.array([])
Ycfc= np.ones((3,3))

for f in Ycfc:
    for comb in range(4):
        if comb == 0:
            ...
        elif comb == 1:
            f[0]= 0
        elif comb == 2:
            f[1]=0
        else: 
            f[2]=0
print()
'''
Mpack = []
iter = 0
M=np.ones((3,3))

for f1 in range(4):
    if f1 == 0:
        continue
    elif f1 ==1:
        M[0,:] = [0,1,1]
    elif f1 ==2:
        M[0,:] = [1,0,1]
    else:
        M[0,:] = [1,1,0]
    for f2 in range(4):
        if f2 == 0:
            continue
        elif f2 == 1:
            M[1,:] = [0,1,1]
        elif f3 == 2:
            M[1,:] = [1,0,1]
        else:
            M[1,:] = [1,1,0]    

        for f3 in range(4):
            Mpack.append(M)
            if f3 == 0:
                continue
            if f3 == 1:
                M[2,:] = [0,1,1]
            elif f3 == 2:
                M[2,:] = [1,0,1]
            else:
                M[2,:] = [1,1,0]    

unicos = []
vistos = set()

for arr in Mpack:
    # chave hashable: pode ser tuple(map(tuple, arr)) ou arr.tobytes()
    chave = arr.tobytes()
    if chave not in vistos:
        vistos.add(chave)
        unicos.append(arr)

print(len(unicos))
for u in unicos:
    print(u)

'''
# 1) todas as linhas possíveis (0/1 com 2 ou 3 uns)
linhas_validas = []
for linha in product([0,1], repeat=3):  # todas as combinações de 3 bits
    if 2 <= sum(linha) <= 3:            # 2 ou 3 uns
        linhas_validas.append(linha)

# 2) formar matrizes combinando 3 linhas
matrizes = []
for l1 in linhas_validas:
    for l2 in linhas_validas:
        for l3 in linhas_validas:
            matriz = np.array([l1, l2, l3])
            matrizes.append(matriz)

print(f"Total de matrizes: {len(matrizes)}")
# exemplo: mostrar as 5 primeiras

matrizes

