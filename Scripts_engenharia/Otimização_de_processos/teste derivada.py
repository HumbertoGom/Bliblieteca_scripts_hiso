def quadrarmenos3xis(x):
    x=x^2 - 3*x
    return x 

h= 2*10**-16

def dervada(funcao(x),x):
    d= (funcao(x + h) - funcao(x) )/h
    print(d)

dervada(quadrarmenos3xis,3)