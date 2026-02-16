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
    
    # Penalidades
    # soluççao por differential evolution não suporta constrainsts, então somamos penalidades altas para impedir restrições de serem violadas.
    #------------
    penalty = 0

    for f in F: #area usada não deve ser maior que area disponivel
        area_usada = Scf[f,:].sum()
        if area_usada < Af[f]:
            penalty+= 1e60
            print('deu merda!\n ELE TIROU AREA DE ONDE NÃO ')

    for c in C:  #água usada não deve exeder a disponível
        agua_usada = Kc * Scf[:,c]
        for f in F:
            if agua_usada[f] < Wf[f]:
                penalty+= 1e60
                print('deu merda!\n ELES  USARAM TUDO! AGORA QUEREM MINHA ÁGUA')

    for f in F:  #não pode cultivar menos que 2 culturas
        if Ycf[f,:].sum() <2: 
            penalty+= 1e60
            print('deu merda!\n TÃO FAZENDO MONOCULTURA! ta virando brasil')

    for f in F:  # se não for mais 20 acres não plantará arroz
        if Scf[f,1]/20 < Ycf[f,1]:
            penalty+= 1e60
            print('deu merda! não estão se dedicando o bastante ao arroz')

    for f in F:
        for c in C:
            if Scf[f,c] > 1e6 * Ycf[f,c]:
                print('deu merda! a binária ta não binária')
                penalty += 1e10

    return -(lucro - penalty)


bounds_Y = [(0,1)]*9
bounds_S = []
for f in range(3):
    for c in range(3):
        bounds_S.append((0, Ac[c]))  # cada cultura c tem área máxima Ac[c]
bounds = bounds_Y + bounds_S
# --------------------
# Otimização com differential_evolution
# --------------------
x0 = np.concatenate([Ycf.ravel(), Scf.ravel()])
result = optimize.differential_evolution(lambda x: -Fobj(x),bounds )

# --------------------
# Reconstruir solução
# --------------------
x_opt = result.x

# arredonda Ycf para binário
Ycf_opt = np.round(x_opt[:9]).reshape(3,3)
Scf_opt = x_opt[9:].reshape(3,3)

print("Lucro máximo:", -result.fun)
print("Ycf otimizado:\n", Ycf_opt)