from pyomo.environ import *

path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

# Sets
model.IDX_i = Set(initialize=['1','2','3','4'])  # clientes
model.IDX_j = Set(initialize=['1','2','3'])      # instalações

# Parameters
model.Cj = Param(model.IDX_j, initialize={'1': 100,'2': 80,'3': 60})   # capacidade
model.Fj = Param(model.IDX_j, initialize={'1': 1000,'2': 800,'3': 600}) # custo fixo
model.di = Param(model.IDX_i, initialize={'1': 50,'2': 40,'3': 30,'4': 20}) # demanda

# Param definido como (i,j)
model.Cij = Param(model.IDX_i, model.IDX_j, initialize={
    ('1','1'): 10, ('1','2'): 14, ('1','3'): 20,
    ('2','1'): 12, ('2','2'):  9, ('2','3'): 16,
    ('3','1'): 20, ('3','2'): 16, ('3','3'): 11,
    ('4','1'): 18, ('4','2'): 20, ('4','3'): 12,
})

# Variables
model.Yj = Var(model.IDX_j, domain=Binary)  
model.Xij = Var(model.IDX_i, model.IDX_j, domain=NonNegativeReals)

# Objective function 
model.obj = Objective(
    expr = sum(model.Yj[j] * model.Fj[j] for j in model.IDX_j) 
         + sum(model.Cij[j,i] * model.Xij[i,j] for j in model.IDX_j for i in model.IDX_i),
    sense=minimize
)

# Constraints

# Cada cliente i deve ter sua demanda atendida
model.con_dem = ConstraintList()
for i in model.IDX_i:
    model.con_dem.add(sum(model.Xij[i,j] for j in model.IDX_j) == model.di[i])

# Capacidade de cada instalação j
model.con_link = ConstraintList()
for j in model.IDX_j:
    model.con_link.add(sum(model.Xij[i,j] for i in model.IDX_i) <= model.Cj[j] * model.Yj[j])

# Solve


solver = SolverFactory('scip', executable=path)
results = solver.solve(model, tee=True)

# Print results
print('\nSolução encontrada:')
for i in model.IDX_i:
    for j in model.IDX_j:
        if model.Xij[i,j].value > 1e-6:  # só mostra valores positivos
            print(f"Cliente {i} atendido pela instalação {j}: {model.Xij[i,j].value}")

for j in model.IDX_j:
    print(f"Instalação {j}: aberta={model.Yj[j].value}")

print("Custo total:", model.obj())