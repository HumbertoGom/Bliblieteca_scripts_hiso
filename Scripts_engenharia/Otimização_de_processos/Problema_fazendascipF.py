from pyomo.environ import *

# solver path (se usar SCIP)
path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

# Sets
model.IDX_f = Set(initialize=['fazenda 1','fazenda 2','fazenda 3'])
model.IDX_c = Set(initialize=['Milho','Arroz','Feijão'])

# Params (dicionários para facilitar M)
Af_dict = {'fazenda 1':400,'fazenda 2':650,'fazenda 3':350}
Wf_dict = {'fazenda 1':1800,'fazenda 2':2200,'fazenda 3':950}
Ac_dict = {'Milho':660,'Arroz':880,'Feijão':400}
Kc_dict = {'Milho':5.5,'Arroz':4,'Feijão':3.5}
Lc_dict = {'Milho':5000,'Arroz':4000,'Feijão':1800}

#inicializando o parametros 
model.Af = Param(model.IDX_f, initialize=Af_dict)
model.Wf = Param(model.IDX_f, initialize=Wf_dict)
model.Ac = Param(model.IDX_c, initialize=Ac_dict)
model.Kc = Param(model.IDX_c, initialize=Kc_dict)
model.Lc = Param(model.IDX_c, initialize=Lc_dict)

# Vars
model.Scf = Var(model.IDX_c, model.IDX_f, domain=NonNegativeReals)
model.Ycf = Var(model.IDX_c, model.IDX_f, domain=Binary)

# Big-M seguro por par (usamos o mínimo entre a área da fazenda e a área máxima da cultura)
#então esse M é o Upper bound
#escrevi desse jeito para ele se ajustar a area de cada fazenda em cada equação
Mdict = {(c,f): min(Af_dict[f], Ac_dict[c]) for c in model.IDX_c for f in model.IDX_f}
model.M = Param(model.IDX_c, model.IDX_f, initialize=1e5, within=NonNegativeReals)

# Objetivo
model.obj = Objective(
    expr = sum(model.Scf[c,f] * model.Lc[c] for c in model.IDX_c for f in model.IDX_f)
           - 5000 * sum(model.Ycf[c,f] for c in model.IDX_c for f in model.IDX_f),
    sense = maximize
)





# Restrições
#escrevi as restrições como função,porque precisamos iterar
def area_rule(m,f):
    return sum(m.Scf[c,f] for c in m.IDX_c) <= m.Af[f]
model.area_const = Constraint(model.IDX_f, rule=area_rule)
# por exemplo precisamos que a area usada seja menor ou igual a área disponível para todo f Pertencente a F.

def cultura_rule(m,c):
    return sum(m.Scf[c,f] for f in m.IDX_f) <= m.Ac[c]
model.cultura_const = Constraint(model.IDX_c, rule=cultura_rule)

def agua_rule(m,f):
    return sum(m.Scf[c,f] * m.Kc[c] for c in m.IDX_c) <= m.Wf[f]
model.agua_const = Constraint(model.IDX_f, rule=agua_rule)

def at_least_two_crops(m,f):
    return sum(m.Ycf[c,f] for c in m.IDX_c) >= 2
model.at_least_two = Constraint(model.IDX_f, rule=at_least_two_crops)

# S <= Y x Up. isso linka as var
def link_rule(m,c,f):
    return m.Scf[c,f] <= m.M[c,f] * m.Ycf[c,f]
model.link = Constraint(model.IDX_c, model.IDX_f, rule=link_rule)

# Y/Up <= S . isso resolve a questão do 0
def link_zero_rule(m,c,f):
    return m.Scf[c,f] >= m.Ycf[c,f]/ m.M[c,f] 
model.linkzero = Constraint(model.IDX_c, model.IDX_f, rule=link_zero_rule)

# mínimo de 20 acres de arroz se plantar arroz 
def arroz_min_rule(m,f):
    return m.Scf['Arroz', f] >= 20 * m.Ycf['Arroz', f]
model.arroz_min = Constraint(model.IDX_f, rule=arroz_min_rule)

# Chamada do solver
solver = SolverFactory('scip', executable=path)
results = solver.solve(model, tee=True)

# Imprime resultados
print("\n--- Solução ---")
for f in model.IDX_f:
    print("Fazenda:", f)
    for c in model.IDX_c:
        print(f"  {c}: Scf = {value(model.Scf[c,f])}, Ycf = {value(model.Ycf[c,f])}")
print("Objetivo:", value(model.obj))

