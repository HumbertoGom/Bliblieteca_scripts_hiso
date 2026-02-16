def fatorial(x, R=1):
    R = x*R
    if x == 1:
        return R
    x-=1 
    return fatorial(x)

print(fatorial(3))