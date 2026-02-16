# Module import
from pyomo.environ import *


path = r"C:\Program Files\SCIPOptSuite 9.2.3\bin\scip.exe"

model = ConcreteModel()

# Variables
model.x = Var( initialize=-1.2,bounds=[0,10], domain = Reals )
model.y = Var( initialize= 1.0,bounds=[0,10], domain = Reals )

# Objective function
model.obj = Objective(
expr= (1-model.x)**2 + 100*(model.y-model.x**2)**2,
sense= minimize )

# Optimization run
solver = SolverFactory('SCIP',executable = path)
results = solver.solve(model,tee=True)

print(' ')
print('Results :')
print('Variable x : ' + str(value(model.x)))
print('Variable y : ' + str(value(model.y)))
print('Objective function : ' + str(value(model.obj)))
print(' ')