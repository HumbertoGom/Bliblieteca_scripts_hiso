# Module import
from pyomo.environ import *


path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

#Sets
model.IDX_f = Set(initialize = ['fazenda 1','fazenda 2','fazenda 3'])
model.IDX_c = Set(initialize = ['Milho','Arroz','Feijão'])

# Parameters

model.Af = Param(model.IDX_f, initialize = {'fazenda 1': 400,'fazenda 2': 650,'fazenda 3': 350}) # Área disponível por fazenda(acre)
model.Wf = Param(model.IDX_f, initialize = {'fazenda 1': 1800,'fazenda 2': 2200,'fazenda 3': 950}) # Água disponível por fazenda(L)

model.Ac = Param(model.IDX_c, initialize = {'Milho':660,'Arroz':880,'Feijão':400}) #área máxima para cada cultura(acre)
model.Kc = Param(model.IDX_c, initialize = {'Milho':5.5,'Arroz':4,'Feijão':3.5}) #consumo de água de cada cultura(L/acre)
model.Lc = Param(model.IDX_c, initialize = {'Milho':5000,'Arroz':4000,'Feijão':1800}) #lucro de cada cultura (R$/acre)

# Variables



model.Scf = Var(model.IDX_c,model.IDX_f, domain= NonNegativeReals)  # area dedicda para cada cultivo em cada fazenda
model.Ycf = Var(model.IDX_c,model.IDX_f, domain = Binary) # quais culturas haveram em cada fazenda,binária


# Objective function

model.obj = Objective(expr = sum(model.Scf[c,f] * model.Lc[c] for c in model.IDX_c for f in model.IDX_f ) - 
                      sum(model.Ycf[c,f]*5000 for c in model.IDX_c for f in model.IDX_f), sense= maximize)

#Constrains

model.conarea = ConstraintList()
for f in model.IDX_f:
    model.conarea.add(sum(model.Scf[c,f] for c in model.IDX_c) >= model.Af[f])

model.conagua = ConstraintList()
for f in model.IDX_f:
    model.conagua.add(sum(model.Kc[c] * model.Scf[c,f] for c in model.IDX_c) >= model.Wf[f])

model.conplant = ConstraintList()
for f in model.IDX_f:
    model.conplant.add(sum(model.Ycf[c,f] for c in model.IDX_c) >= 2)

model.conlink = ConstraintList()
for f in model.IDX_f:
    for c in model.IDX_c:
        model.conlink.add( model.Scf[c,f] <= model.Ycf[c,f] * 1e8)

model.conarroz = ConstraintList()
for f in model.IDX_f:
    model.conarroz.add(model.Scf['Arroz',f]/20 >= model.Ycf['Arroz',f]) 

# Optimization run
solver = SolverFactory('SCIP',executable = path)
results = solver.solve(model,tee=True)

print("\n--- Resultados ---")

# Valores de Scf (área plantada)
for c in model.IDX_c:
    for f in model.IDX_f:
        print(f"Scf[{c}, {f}] = {model.Scf[c,f].value}")

# Valores de Ycf (binária de plantio)
for c in model.IDX_c:
    for f in model.IDX_f:
        print(f"Ycf[{c}, {f}] = {model.Ycf[c,f].value}")

# Valor da função objetivo
print("\nLucro total:", model.obj())