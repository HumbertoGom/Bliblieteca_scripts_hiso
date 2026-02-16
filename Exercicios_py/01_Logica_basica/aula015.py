def produtos(*args):
    resultado =1 
    for numero in args:
        resultado *= numero
    print(resultado)
    return resultado

def sendo_par(x):
    if x%2 == 0:
        print(f'o número {x} é par')
        return 'par'
    
    else:
        print(f'o número {x} é impar')
        return 'impar'
    
print(sendo_par(3))

produtos(3,4,5,6,7,8,9,10)