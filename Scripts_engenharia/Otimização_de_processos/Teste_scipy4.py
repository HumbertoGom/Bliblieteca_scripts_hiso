from scipy import integrate,optimize

def func(x):
    f= (1-x[0])*2+100*(x[1]-x[0]**2)**2
    return f

#função de rosen é conhecida .rosen
sol_BFGS = optimize.minimize(optimize.rosen,[0,0],method='L-BFGS-B', bounds=[[2,10],[2,10]])
print(sol_BFGS)

