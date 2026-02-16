'''
from pyomo.environ import *

# solver path
path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

#indice tintas
model.IDX_T = Set(initialize=['tintaA','tintaB','tintaC','inerte'])

#Params

model.Et = Param(model.IDX_T,intialize =[500,250,100,1e6]) #estoque de tintas
model.XCAROt = Param(model.IDX_T,intialize =[0.10,0.05,0.05,0.8]) # composição tinta cara
model.XBAROt = Param(model.IDX_T,intialize =[0.15,.10,0,0.75]) #comp tinta barata
model.PCARO = Param(initialize= 1.0)
model.PBARO = Param(initialize= 0.6)
model.Pinert = Param(initialize= 0.1)


# Vars
model.ProdCARO = Var(domain=NonNegativeReals) # produção do caro em Kg
model.ProdBARO = Var(domain=NonNegativeReals) # produção do aditivo barato em Kg

#Função objetivo

model.obj = Objective(expr= model.ProdCARO * model.PCARO  #ganho do caro
                    +  model.ProdBARO * model.PBARO  #ganho do barato
                      - 0.1*(model.ProdCARO*model.XCAROt[3]+model.ProdBARO*model.XBAROt[3])  #custos do inerte
                      
                      ,sense= maximize)

#restrições

def estoque(t):
    return model.Et[t] <= model.ProdCARO*model.XCAROt[t]+model.ProdBARO*model.XBAROt[t]
model.estoque_cons = Constraint(model.IDX_T, rule=estoque)

'''

from pyomo.environ import *
from pyomo.environ import value

# Caminho do solver
path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

# Índices de matérias-primas
model.IDX_T = Set(initialize=['A', 'B', 'C', 'inerte'])

# Parâmetros
model.Et = Param(model.IDX_T, initialize={
    'A': 500,
    'B': 250,
    'C': 100,
    'inerte': 1e6  # inerte ilimitado
})

model.XCAROt = Param(model.IDX_T, initialize={
    'A': 0.10,
    'B': 0.05,
    'C': 0.05,
    'inerte': 0.80
})

model.XBAROt = Param(model.IDX_T, initialize={
    'A': 0.15,
    'B': 0.10,
    'C': 0.0,
    'inerte': 0.75
})

model.PCARO = Param(initialize=1.0)
model.PBARO = Param(initialize=0.6)
model.Pinert = Param(initialize=0.1)

# Variáveis
model.ProdCARO = Var(domain=NonNegativeReals)
model.ProdBARO = Var(domain=NonNegativeReals)

# Função objetivo (maximizar lucro)
def lucro(model):
    receita = model.ProdCARO * model.PCARO + model.ProdBARO * model.PBARO
    custo_inerte = model.Pinert * (
        model.ProdCARO * model.XCAROt['inerte'] +
        model.ProdBARO * model.XBAROt['inerte']
    )
    return receita - custo_inerte

model.obj = Objective(rule=lucro, sense=maximize)

# Restrições de estoque
def estoque_rule(model, t):
    # uso de t <= estoque de t
    return model.ProdCARO * model.XCAROt[t] + model.ProdBARO * model.XBAROt[t] <= model.Et[t]

model.estoque_cons = Constraint(model.IDX_T, rule=estoque_rule)

# Resolver
solver = SolverFactory('scip', executable=path)
resultado = solver.solve(model, tee=True)


# Exibir resultados
print("\nRESULTADOS:")
print(f"Produção aditivo caro: {model.ProdCARO():.2f} kg")
print(f"Produção aditivo barato: {model.ProdBARO():.2f} kg")

for t in model.IDX_T:
    consumo = value(model.ProdCARO) * value(model.XCAROt[t]) + value(model.ProdBARO) * value(model.XBAROt[t])
    print(f"O consumo da tinta {t} é de {consumo:.2f} kg")

print(f"Lucro total: {model.obj():.2f} $")
