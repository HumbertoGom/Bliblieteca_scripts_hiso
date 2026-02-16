
lista = [ 2, 1 ,2]
l2= [8,8,8,1, 8,8,8]
l3= [5,3,1,1,1,2,1]

'''
exemplos=[[1,2,1],            # 1 aparece 2 vezes; 2 aparece 1 → majoritário = 1
[3,3,4,3,5],        # 3 aparece 3 vezes num array de 5 → majoritário = 3
[0,0,1,0],
[4,4,4,4,4,2,2,4,3,4,5,4,4,4]   # majoritário = 4
[6,6,1,6,2,6,3,6,6,6,7,6,8]     # majoritário = 6
[10,9,10,10,10,8,10,7,10,6,10]]  # majoritário = 10          # 0 aparece 3 vezes num array de 4 → majoritário = 0]
'''

def maj(num):
    repet=0
    n=len(num)
    for elem in num:
        for elem2 in num:
            if elem == elem2:
                repet +=1
            if repet >= n/2:
                return elem2
    
print(maj([10,9,10,10,10,8,10,7,10,6,10]))