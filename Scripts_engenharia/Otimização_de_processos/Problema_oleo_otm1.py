from pyomo.environ import *

# solver path 
path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

# Sets
model.IDX_P = Set(initialize=['oleo 1' , 'oleo 2' , 'oleo 3', 'oleo 4'])
model.IDX_G = Set(initialize=['Superazul','Azul','Amarelo'])

# Param

model.Qp = Param(model.IDX_P, initialize = { 'oleo 1':3500 ,'oleo 2': 2200 ,'oleo 3':4200 ,'oleo 4':1800})
model.Cp = Param(model.IDX_P, initialize = { 'oleo 1':19 ,'oleo 2': 24 ,'oleo 3':20 ,'oleo 4':27})

model.Cg = Param(model.IDX_G, initialize = {'Superazul':35,'Azul':28,'Amarelo':22})

# vars

model.Xpg = Var(model.IDX_P,model.IDX_G, domain = NonNegativeReals )

#objetivo

model.Obj = Objective(expr= sum(model.Qp[p] * model.Cp[p] for p in model.IDX_P)   + 
                      sum(model.Xpg[p,g] * model.Cg[g] for p in model.IDX_P for g in model.IDX_G), sense = minimize)

#restrições 

model.comp1 = Constraint(expr= model.Xpg['oleo 1','Superazul'] <= 0.3* sum(model.Xpg[p,'Superazul'] for p in model.IDX_P))
model.comp2 = Constraint(expr= model.Xpg['oleo 2','Superazul'] >= 0.4* sum(model.Xpg[p,'Superazul'] for p in model.IDX_P))
model.comp3 = Constraint(expr= model.Xpg['oleo 3','Superazul'] <= 0.5* sum(model.Xpg[p,'Superazul'] for p in model.IDX_P))

model.comp4 = Constraint(expr= model.Xpg['oleo 1','Azul'] <= 0.3* sum(model.Xpg[p,'Azul'] for p in model.IDX_P))
model.comp5 = Constraint(expr= model.Xpg['oleo 2','Azul'] >= 0.1* sum(model.Xpg[p,'Azul'] for p in model.IDX_P))

model.comp6 = Constraint(expr= model.Xpg['oleo 1','Amarelo'] <= 0.7* sum(model.Xpg[p,'Amarelo'] for p in model.IDX_P))

model.balmass = ConstraintList()
for p in model.IDX_P:
    model.balmass.add(model.Qp[p] == sum(model.Xpg[p,g] for g in model.IDX_G))


solver = SolverFactory('scip', executable=path)
solver.solve(model, tee=True)


for p in model.IDX_P:
    for g in model.IDX_G:
        print(f"Xpg[{p},{g}] = {model.Xpg[p,g].value}")