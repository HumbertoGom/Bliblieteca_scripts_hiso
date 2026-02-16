from pyomo.environ import *

# solver path (se usar SCIP)
path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

# Sets
model.IDX_f = Set(initialize=['fabrica1','fabrica2','fabrica3'])
model.IDX_c = Set(initialize=['C1','C2','C3','C4','C5','C6'])
model.IDX_s = Set(initialize=['semana1','semana2','semana3','semana4'])

# Params 


#custo de produção (R$/ton)
KPfsDict = {
    ('fabrica1', 'semana1'): 200, ('fabrica1', 'semana2'): 205, ('fabrica1', 'semana3'): 210, ('fabrica1', 'semana4'): 200,
    ('fabrica2', 'semana1'): 180, ('fabrica2', 'semana2'): 175, ('fabrica2', 'semana3'): 185, ('fabrica2', 'semana4'): 190,
    ('fabrica3', 'semana1'): 190, ('fabrica3', 'semana2'): 190, ('fabrica3', 'semana3'): 195, ('fabrica3', 'semana4'): 200
}


model.KPfs = Param(model.IDX_f,model.IDX_s, initialize=KPfsDict) 

# Custo de transporte Fábrica → Cliente (R$/ton)
KTfcDict = {
    ('fabrica1', 'C1'): 40, ('fabrica1', 'C2'): 55, ('fabrica1', 'C3'): 60, ('fabrica1', 'C4'): 45, ('fabrica1', 'C5'): 70, ('fabrica1', 'C6'): 50,
    ('fabrica2', 'C1'): 35, ('fabrica2', 'C2'): 40, ('fabrica2', 'C3'): 45, ('fabrica2', 'C4'): 55, ('fabrica2', 'C5'): 65, ('fabrica2', 'C6'): 60,
    ('fabrica3', 'C1'): 50, ('fabrica3', 'C2'): 60, ('fabrica3', 'C3'): 55, ('fabrica3', 'C4'): 40, ('fabrica3', 'C5'): 45, ('fabrica3', 'C6'): 65
}

model.KTfc = Param(model.IDX_f, model.IDX_c, initialize=KTfcDict)

# Parâmetro KAcs: preço/custo associado ao cliente por semana (R$/ton)
KAcsDict = {
    ('C1', 'semana1'): 300, ('C1', 'semana2'): 280, ('C1', 'semana3'): 310, ('C1', 'semana4'): 290,
    ('C2', 'semana1'): 300, ('C2', 'semana2'): 300, ('C2', 'semana3'): 320, ('C2', 'semana4'): 310,
    ('C3', 'semana1'): 290, ('C3', 'semana2'): 270, ('C3', 'semana3'): 300, ('C3', 'semana4'): 280,
    ('C4', 'semana1'): 310, ('C4', 'semana2'): 290, ('C4', 'semana3'): 310, ('C4', 'semana4'): 295,
    ('C5', 'semana1'): 320, ('C5', 'semana2'): 310, ('C5', 'semana3'): 330, ('C5', 'semana4'): 310,
    ('C6', 'semana1'): 300, ('C6', 'semana2'): 285, ('C6', 'semana3'): 295, ('C6', 'semana4'): 280
}

model.KAcs = Param(model.IDX_c, model.IDX_s, initialize=KAcsDict)

# Parâmetro Rs: preço por semana (R$/ton)
RsDict = {
    'semana1': 500,
    'semana2': 520,
    'semana3': 480,
    'semana4': 510
}

model.Rs = Param(model.IDX_s, initialize=RsDict)

# Parâmetros D-cs e D+cs - demanda mínima e máxima de cada cliente por semana
# Parâmetro D-cs (mínimo)
D_menos_cs_Dict = {
    ('C1', 'semana1'): 12, ('C1', 'semana2'): 8,  ('C1', 'semana3'): 15, ('C1', 'semana4'): 10,
    ('C2', 'semana1'): 18, ('C2', 'semana2'): 10, ('C2', 'semana3'): 20, ('C2', 'semana4'): 16,
    ('C3', 'semana1'): 14, ('C3', 'semana2'): 12, ('C3', 'semana3'): 16, ('C3', 'semana4'): 10,
    ('C4', 'semana1'): 10, ('C4', 'semana2'): 6,  ('C4', 'semana3'): 12, ('C4', 'semana4'): 14,
    ('C5', 'semana1'): 15, ('C5', 'semana2'): 13, ('C5', 'semana3'): 10, ('C5', 'semana4'): 12,
    ('C6', 'semana1'): 10, ('C6', 'semana2'): 10, ('C6', 'semana3'): 14, ('C6', 'semana4'): 12
}

model.D_menos = Param(model.IDX_c, model.IDX_s, initialize=D_menos_cs_Dict)

# Parâmetro D+cs (máximo)
D_mais_cs_Dict = {
    ('C1', 'semana1'): 20, ('C1', 'semana2'): 18, ('C1', 'semana3'): 25, ('C1', 'semana4'): 18,
    ('C2', 'semana1'): 25, ('C2', 'semana2'): 20, ('C2', 'semana3'): 28, ('C2', 'semana4'): 22,
    ('C3', 'semana1'): 22, ('C3', 'semana2'): 20, ('C3', 'semana3'): 24, ('C3', 'semana4'): 18,
    ('C4', 'semana1'): 18, ('C4', 'semana2'): 16, ('C4', 'semana3'): 20, ('C4', 'semana4'): 22,
    ('C5', 'semana1'): 24, ('C5', 'semana2'): 22, ('C5', 'semana3'): 20, ('C5', 'semana4'): 23,
    ('C6', 'semana1'): 18, ('C6', 'semana2'): 18, ('C6', 'semana3'): 22, ('C6', 'semana4'): 20
}

model.D_mais = Param(model.IDX_c, model.IDX_s, initialize=D_mais_cs_Dict)

# Parâmetro Ecc - estoque de cada cliente
EccDict = {
    'C1': 20, 'C2': 20, 'C3': 20,
    'C4': 20, 'C5': 20, 'C6': 20
}

model.Ecc = Param(model.IDX_c, initialize=EccDict)

# Parâmetro Eff: capacidade de estoque por fábrica (ton)
EffDict = {
    'fabrica1': 50,
    'fabrica2': 80,
    'fabrica3': 60
}

model.Eff = Param(model.IDX_f, initialize=EffDict)

# Parâmetro Pf: produção máxima por fábrica (ton)
PfDict = {
    'fabrica1': 70,
    'fabrica2': 80,
    'fabrica3': 90
}

model.Pf = Param(model.IDX_f, initialize=PfDict)

# Parâmetro KCC: custo de armazenamento por cliente (R$/ton)
model.KCCs = Param(model.IDX_c, initialize=10)

# Parâmetro KFF: custo de armazenamento por fábrica (R$/ton)
model.KFFs = Param(model.IDX_f, initialize=10)


#variáveis

# Variável binária: cliente atendido em cada semana
model.y = Var(model.IDX_c, model.IDX_s, domain=Binary)

# Variável contínua: quantidade transportada de fábrica -> cliente na semana (ton)
model.q = Var(model.IDX_f, model.IDX_c, model.IDX_s, domain=NonNegativeReals)

# Variável contínua: fração da capacidade máxima de produção usada (0 ≤ x ≤ 1)
model.x = Var(model.IDX_f, model.IDX_s, bounds=(0,1))

# Variável contínua: quantidade aramazenada na fábrica
model.AFFs = Var(model.IDX_f,model.IDX_s, domain=NonNegativeReals, bounds=(0,model.Eff))

model.ACCs = Var(model.IDX_c,model.IDX_s, domain=NonNegativeReals, bounds=(0,model.Ecc))

#função Obj

model.obj = Objective(
    expr = (sum(model.q[f,c,s] for f in model.IDX_f for c in model.IDX_c)[s] * model.Rs[s] for s in model.IDX_s) #receita vezes qtd enviada
    -sum(model.KPfs[f,s] * model.x[f,s] * model.Pf[f] for f in model.IDX_f for s in model.IDX_s ) # custos de produção
    -sum(model.KTfc[f,c] * model.q[f,c,s] for f in model.IDX_f for c in model.IDX_c for s in model.IDX_s) #custo de transporte
    -sum(model.Ka[c,s]* model.y[c,s] for s in model.IDX_s for c in model.IDX_c)     #custo ativação de cliente
    
    -sum(model.AFFs[s,f] * model.KFFs[f] for f in model.IDX_f for s in model.IDX_s) # custo de armazenamento da fabrica
    -sum(model.ACCs[s,c] * model.KCCs[c] for c in model.IDX_c for s in model.IDX_s) # custo de armazenamento cliente
)

#RESTRIÇÕES

def capacidade_producao_rule(model, f, s):
    return sum(model.q[f,c,s] + model.ACCs[c] for c in model.IDX_c) <= model.Pf[f] * model.x[f,s]

model.capacidade_producao = Constraint(model.IDX_f, model.IDX_s, rule=capacidade_producao_rule)


def atendimento_rule(model, c, s):
    return sum(model.q[f,c,s] for f in model.IDX_f) <= model.D_mais[c,s] * model.y[c,s]

model.atendimento = Constraint(model.IDX_c, model.IDX_s, rule=atendimento_rule)
