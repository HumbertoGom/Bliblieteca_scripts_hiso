'''
soma=0

for i in range(1,11):
    soma+=(2*i +1)
r1=120
'''

'''
prod1= 1
for i in range(1,9):
    if i%2 ==0:
        prod1 *=i
r2=384
'''
'''
soma =0
for i in range(1,4):
    prod2= 1
    for j in range(1,3):
        prod2*=(i+j)
    soma+=prod2


R3=38
'''

prod3 = 1
for i in range(1,4):
    soma3=0 
    for j in range (1,i+1):
        soma3+=j
    prod3*=soma3

print(prod3)