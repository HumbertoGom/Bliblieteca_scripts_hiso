from scipy import integrate,optimize

f = lambda x:x**4 + x**2 -x
g = lambda x:x*(x-2)*(x+2)**2

print('soluções para f')

xsol_BR= optimize.minimize_scalar(f,bracket=[-2,2],method='brent')
print(xsol_BR)
xsol_GO= optimize.minimize_scalar(f,bracket=[-2,2],method='golden')
print('\n\n',xsol_GO)

print('soluções para g \n\n\n\n')

xsol_BRg= optimize.minimize_scalar(g,bracket=[-3,2],method='brent')
print(xsol_BRg)
xsol_GOg= optimize.minimize_scalar(g,bracket=[-3,2],method='golden')
print('\n\n',xsol_GOg)