'''
D=2
H=4

V= 3.14 * (D/2)^2 * H

disp(V)
# nah,isso facil demais 4/9/2025 tenho mais habilidade que isso
'''

'''
def analise_risco():
    D=100
    x1=150
    y1=-20
    x=int(input('Digite a Coordenada X do ponto'))
    y=int(input('Digite a Coordenada Y do ponto'))
    dist = ( (x1-x)**2  +  (y1-y)**2 )**0.5
    print (dist)
    if dist > D:
        print('esta seguro da explosão')
    else:
        print('se fudeu,virou carvão')

while True :
    analise_risco()
    '''

def resolveSeg():
    print('Com uma equação de segundo grau na forma ax^2+bx+c\n digite cada parametro')
    a=int(input('digite o valor de A'))
    b=int(input('digite o valor de B'))
    c=int(input('digite o valor de C'))
    descri= b**2 - (4*a*c)
    raiz1 = (-b + descri**0.5)/(2*a)
    raiz2 = (-b - descri**0.5)/(2*a)

    if descri >= 0:
        print('essa eq possui raiz real')
        if descri == 0:
            print('são duas raizes reais iguais')
        else:
            print('são duas raizes reais differentes')
    else:
        print('essa equação não possui raizes reais')
    print(f'a raiz 1 é {raiz1}\n a raiz 2 é {raiz2}')

resolveSeg()