#integral numerica 1
def func(x):
    return 1/(1+x)

def trapezioS(func,a,b):
    Area= (b-a)*(0.5*func(a)+0.5*func(b))
    return Area

print (trapezioS(func,0,1))

def trapezioCom(f,a,b,n):
    dx=(b-a)/n
    soma = 0
    for i in range(1,n-1):
        soma+= f(i)
    Area = dx*(((f(a)+f(b))/2)+soma)
    return Area

print(trapezioCom(func,1,0,4))