import numpy as np
from scipy import optimize

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
def Fobj_penalizada(x):
    Ycf = x[:9].reshape(3,3)
    Scf = x[9:].reshape(3,3)

    ganho = (Lc * Scf).sum()
    custo = 5000 * Ycf.sum()
    lucro = ganho - custo

    penalty = 0

    # área
    for f in F:
        penalty += max(0, Scf[f,:].sum() - Af[f]) * 1e6

    # água
    for f in F:
        penalty += max(0, (Scf[f,:]*Kc).sum() - Wf[f]) * 1e6

    # pelo menos 2 culturas
    for f in F:
        penalty += max(0, 2 - np.round(Ycf[f,:]).sum()) * 1e6

    # arroz mínimo 20 acres
    for f in F:
        if Ycf[f,1] > 0.5 and Scf[f,1] < 20:
            penalty += 1e6

    # coerência Scf x Ycf
    for f in F:
        for c in C:
            if Scf[f,c] > Af[f]*Ycf[f,c]:
                penalty += 1e6

    return -(lucro - penalty)

#==============
# chamada do DE
#------------

bounds_Y = [(0,1)]*9
bounds_S = []
for f in F:
    for c in C:
        bounds_S.append((0, Af[f]))  # garante que soma ≤ Af[f]
bounds = bounds_Y + bounds_S

result = optimize.differential_evolution(Fobj_penalizada, bounds)


x_opt = result.x

# Binária
Ycf_opt = np.round(x_opt[:9]).reshape(3,3).astype(int)

# Contínua
Scf_opt = x_opt[9:].reshape(3,3)

# Zera áreas onde não tem plantio
Scf_opt[Ycf_opt == 0] = 0

# Ajuste visual
np.set_printoptions(precision=1, suppress=True)

print("Lucro máximo:", -result.fun)
print("Ycf otimizado:\n", Ycf_opt)
print("Scf otimizado:\n", Scf_opt)

