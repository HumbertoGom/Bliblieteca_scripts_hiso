import random

#mapa = [ 0 for i in range(6)]
#mapa = [mapa for i in range(6)]

mapa= [[0 for _ in range(6)] for _ in range(6)]

print(*mapa,sep='\n')
def inserir_navio_de2(mapa):
    if random.randint(0,1):
        # inserção horizontal
        linha_esc = random.randint(0,5)
        pos_esc = random.randint(0,4) # não pode na pos 5 pq sairia do mapa
        print(linha_esc,pos_esc)
        mapa[linha_esc][pos_esc] = 1
        mapa[linha_esc][pos_esc+1] = 1
    else:
        print('inserção vertical')
        #inserção verticical
        coluna_esc = random.randint(0,5)
        linha_esc = random.randint(0,4)  #vai ser gerado da linha esc para baixo
        mapa[linha_esc][coluna_esc] = 1
        mapa[linha_esc+1][coluna_esc] = 1




'''
def inserir_navio_de3(mapa):
    if random.randint(0,1):
        # inserção horizontal
        linha_esc = random.randint(0,5)
        pos_esc = random.randint(0,3) # não pode na pos 5 pq sairia do mapa

        #checkar se a tile está vazia antes de colocar
        while (mapa[linha_esc][pos_esc] + mapa[linha_esc][pos_esc+1] + mapa[linha_esc][pos_esc+2]) >0:
            linha_esc = random.randint(0,5)    
            pos_esc = random.randint(0,3)
        mapa[linha_esc][pos_esc] = 1
        mapa[linha_esc][pos_esc+1] = 1
        mapa[linha_esc][pos_esc+2] = 1
    else:
        print('inserção vertical de 3')
        #inserção verticical
        coluna_esc = random.randint(0,5)
        linha_esc = random.randint(0,3)  #vai ser gerado da linha esc para baixo
        mapa[linha_esc][coluna_esc] = 1
        mapa[linha_esc+1][coluna_esc] = 1
        mapa[linha_esc+2][coluna_esc] = 1
'''

#inserir_navio_de2(mapa)

print('mapa depois inserção')
print(*mapa,sep='\n')

#print(*mapa,sep='\n')
