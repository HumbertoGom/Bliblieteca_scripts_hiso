import numpy as np
from scipy import optimize

f1= lambda x: x[0]+x[1]-7
f2= lambda x : x[0]**2 +x[1]**2 - 25

def func(x):
    f1=  x[0]+x[1]-7
    f2=  x[0]**2 +x[1]**2 - 25
    f= [f1,f2]
    return f
x0 = [0,0]

Xsol_HY = optimize.root(func,x0)
print(Xsol_HY)
Xsol_KR = optimize.root(func,x0,method='krylov')
print('\n\n',Xsol_KR)