from itertools import count

c1= count(102)

for i in c1:
    if i % 7 ==0 and i % 23==0 and i % 101==0 :
        print(i, 'é divisível por 7, 23 e 101')
        prox= input('deseja ver o proximo?')
        if prox == 'S':
            continue
        else:
            break