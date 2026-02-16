# exercicio da aula de intro II.

s=0
produtorio= 1 
for i in range(3):
    i+=1
    for j in range(3):
        j+= 10 
        produtorio *= (i+j)
    s+= produtorio
    produtorio = 1
print(s)