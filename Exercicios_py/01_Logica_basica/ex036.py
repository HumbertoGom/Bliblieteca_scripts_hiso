
'''
result = 0

for i in range(1,4):
    for j in range(1,3):
        result +=(i+j)
print (result)
'''
'''produto = 1

for i in range(1,4):
    soma = 0
    for j in range(1,3):
        soma+= i*j
    produto*=soma

print(produto)


'''

soma=0
for i in range(1,4):
    produto= 1
    for j in range (1,i+1):
        produto*=j
    soma+=produto

print(soma)