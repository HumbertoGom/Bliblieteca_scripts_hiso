e = 2.71828

def func(x):
    return e**-x - x

def numder(x, f):
    dx = 0.000001
    return (f(x + dx) - f(x - dx)) / (2 * dx)

def NrUni(x, f):
    IT = 0
    ITmax = 100
    tol = 0.000001
    x0 = x
    f0 = f(x0)
    while IT < ITmax and abs(f0) > tol:
        print(f"Iteração {IT}: x = {x0:.6f}, f(x) = {f0:.6f}")
        df0 = numder(x0, f)
        passo = -f0 / df0
        x1 = x0 + passo
        f1 = f(x1)
        if abs(f1) > abs(f0):
            passo = -f0 / (df0 * 2)
            x1 = x0 + passo
            f1 = f(x1)
        x0 = x1
        f0 = f1
        IT += 1
    return (x0, f0, IT)

U = NrUni(2.0, func)
print("\nResultado final:", U)