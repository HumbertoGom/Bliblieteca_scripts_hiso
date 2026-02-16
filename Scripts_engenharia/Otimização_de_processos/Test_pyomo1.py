from pyomo.environ import *

model = ConcreteModel()
model.x = Var(initialize=-1.2, domain=Reals)
model.y = Var(initialize=-1.2, domain=Reals)

model.obj = Objective(
    expr=(1 - model.x)**2 + 100*(model.y - model.x**2)**2,
    sense=minimize
)

# caminho completo para o executável ipopt.exe
solver = SolverFactory('ipopt', executable=r"C:\ipopt\bin\ipopt.exe")

results = solver.solve(model, tee=True)

print('Results:')
print('x =', value(model.x))
print('y =', value(model.y))
print('Objective =', value(model.obj))
