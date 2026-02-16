C = int(input('qual o numero de carbonos'))
H = int(input('qual o numero de Hidrogenios'))
if H == 2*C + 2:
    print('é um alcano')
    Numch2= C-2
    print('CH3-','CH2-'*Numch2,'CH3',sep='')
    
elif H== 2*C:
    print('é um alceno')
elif H== 2*C -2:
    print('é um alcino')