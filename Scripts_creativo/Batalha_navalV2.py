#Projeto pessoal para prática de código python
#O Script faz um jogo de batalha naval,que é jogado por input do usario
#o jogo esta completo,funcional ,e tem opção de difficuldades

import random

mapa= [[0 for _ in range(6)] for _ in range(6)]
#mapa criado como uma matriz 6x6 de 0s. 
#sera colocado 1 onde tem navio.
#quando atira em um espaço é somado 2,assim vazio se torna 2,e navio 3.
#0 - água ; 1 - navio ; 2- tiro caiu na água 3- tiro acertou o návio


def inserir_horizonatal(mapa,length):
    #primeiro chute
    linha_esc = random.randint(0,5)
    coluna_esc = random.randint(0,6-length)

    #checkar se as tiles estão vazias
    posicoes = [mapa[linha_esc][coluna_esc+i] for i in range(length)]
    while sum(posicoes) > 0: #esse loop ira repetir todas as pos selecionadas serem 0
        linha_esc = random.randint(0,5)
        coluna_esc = random.randint(0,6-length)
        posicoes = [mapa[linha_esc][coluna_esc+i] for i in range(length)]

    #alterar os valores    
    for i in range(length):
        mapa[linha_esc][coluna_esc+i] = 1

def inserir_vertical(mapa,length):
    #primeiro chute
    coluna_esc = random.randint(0,5)
    linha_esc = random.randint(0,6-length)  #vai ser gerado da linha esc para baixo  
    posicoes =  [mapa[linha_esc+i][coluna_esc] for i in range(length)]

    #checkar se estão vazias
    while sum(posicoes) > 0: 
        coluna_esc = random.randint(0,5)
        linha_esc = random.randint(0,6-length)
        posicoes = [mapa[linha_esc+i][coluna_esc] for i in range(length)]

    #alterar valores
    for i in range(length):
        mapa[linha_esc+i][coluna_esc] = 1 

def inserir_navio_de2(mapa):
    if random.randint(0,1):
        inserir_horizonatal(mapa,2)
    else:
        inserir_vertical(mapa,2)

def inserir_navio_de3(mapa):
    if random.randint(0,1):
        inserir_horizonatal(mapa,3)
    else:
        inserir_vertical(mapa,3)

def inserir_navio_de4(mapa):
    if random.randint(0,1):
        inserir_horizonatal(mapa,4)
    else:
        inserir_vertical(mapa,4)

def inserir_navio_de5(mapa):
    if random.randint(0,1):
        inserir_horizonatal(mapa,5)
    else:
        inserir_vertical(mapa,5)





def difficulty_selection():
    print('[Easy]: 30 cannoballs e 3 barcos')
    print('[Normal]: 22 Cannolballs e 5 barcos')
    print('[Hard]:18 cannonballs e 6 barcos(2x1)')
    escolha = input('escolha uma difficuldade')
    if escolha.capitalize() == 'Easy':
        cannonballs = 30
        inserir_navio_de5(mapa)
        inserir_navio_de4(mapa)
        inserir_navio_de2(mapa)
        return cannonballs
    
    elif escolha.capitalize() == 'Normal':
        cannonballs = 22
        inserir_navio_de2(mapa)
        inserir_navio_de3(mapa)
        inserir_navio_de4(mapa)
        inserir_navio_de5(mapa)
        return cannonballs 
    
    elif escolha.capitalize() == 'Hard':
        cannonballs = 18
        inserir_navio_de2(mapa)
        inserir_navio_de2(mapa)
        inserir_navio_de2(mapa)
        inserir_navio_de2(mapa)
        inserir_navio_de2(mapa)
        inserir_navio_de2(mapa)
        print('boa sorte, voçê escolheu Hard')
        return cannonballs
    
    else: 
        print(f'{escolha} não é uma difficuldade válida\nDigite uma difficuldade válida\n\n')
        return difficulty_selection()


cannonballs = difficulty_selection()
def ABC_to_012(letter):
    if letter == 'A':
        return 0
    if letter == 'B':
        return 1
    if letter == 'C':
        return 2
    if letter == 'D':
        return 3
    if letter == 'E':
        return 4
    if letter == 'F':
        return 5
def display_mapa(mapa):
    i=0
    print('',0,1,2,3,4,5)
    for line in mapa:
        print(ABC[i],sep='',end='')
        i+=1
        for space in line:
            if space == 0:
                print('?',sep='',end=' ')
            if space == 1:
                print('?',sep='',end=' ')
            elif space == 2:
                print('X',sep='',end=' ')
            elif space == 3:
                print('B',sep='',end=' ')
            elif space >=4:
                print('Z',sep='',end=' ')
        print('')
    print(f'Balas de canhão sobrando: {cannonballs}')

ABC = 'ABCDEF'
while cannonballs >0 :
#    print('mapa na memória',*mapa,sep='\n')
    print('')
    display_mapa(mapa)
    
    Proximo_Tiro = input('Digite uma posição para priximo tiro, exemplo (A0) ')
    #Validação do tiro
    if Proximo_Tiro[0] in ABC and Proximo_Tiro[1].isnumeric():
        print('valor válido')
        Tiro_X = int(Proximo_Tiro[1])
        Tiro_Y = ABC_to_012(Proximo_Tiro[0])
        pos_tiro = mapa[Tiro_Y][Tiro_X]

        #checkar em qual espaço caiu
        if pos_tiro == 3 or pos_tiro == 2:
            print('ja atirou aqui \nmire denovo')
        if pos_tiro == 1:
            print('Navio atingido')
            cannonballs-=1 
            mapa[Tiro_Y][Tiro_X]+=2
        if pos_tiro == 0:
            print('Caiu no mar...')
            cannonballs-=1 
            mapa[Tiro_Y][Tiro_X]+=2  
    else:
        print('valor inválido')
    if all(1 not in linha for linha in mapa):
        print('YOU WIN\n\n\n\n\n YOU WIIN')
        break
    if cannonballs == 0:
        print('Voçê perdeu')




