from scipy import optimize
import numpy as np

#criação das funções
lhs = lambda x:-x
rhs = lambda x:np.log(x)
# ln(x) - x
eq= lambda x:lhs(x) - rhs(x)
deq = lambda x: -1 -1/ x

#intervalos
a=1e-6
b=1

print('Metodo de brent')
Xsol_BR = optimize.root_scalar(eq,method='brentq',bracket=[a,b])
print (Xsol_BR)

print('\nBisseção')
Xsol_BS = optimize.root_scalar(eq,method='bisect',bracket=[a,b])
print (Xsol_BS)

#resultado do problema
raiz = Xsol_BS.root

print('\n\n\n')
#metodo NR x Secante
print('Newton-Rhapson')
Xsol_NR = optimize.root_scalar(eq,method='newton',x0=(a+b)/2,fprime=deq)
print(Xsol_NR)
print('\nSecante')
Xsol_SE = optimize.root_scalar(eq,method='secant',x0=a,x1=b)
print(Xsol_SE)