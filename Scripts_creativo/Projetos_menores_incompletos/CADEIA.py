

cadeia = [[1,1,1,2],
          [1,1,1,2]]
#1 para ligação com H
#2 para simples com outro C
#3 para dupla com outro C
#4 para tripla com outro C


for i in cadeia:
    H=0
    grupo = 'C'
    for j in i:
        if j == 1: # se cada ligação é com Hidrogenio
            H+=1
        elif j==2: # se a ligação é com outro carbono
            ligacao='-'
        elif j==3:
            ligacao= '=' # se a ligação for dupla

        
    print(f'{grupo}H{H}{ligacao}',end='')