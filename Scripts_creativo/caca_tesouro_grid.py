import random

mapa= [[0 for _ in range(6)] for _ in range(6)]


#player start
mapa[2][2] = 3

def inserir_tesouro(map,n):
    for i in range(n):
        chosen_line = random.randint(0,5)
        chosen_row = random.randint(0,5)
        while mapa[chosen_line][chosen_row] is not 0:
            chosen_line = random.randint(0,5)
            chosen_row = random.randint(0,5)
        mapa[chosen_line][chosen_row] = 1




def inserir_armadilhas(map,n):
    for i in range(n):
        chosen_line = random.randint(0,5)
        chosen_row = random.randint(0,5)
        while mapa[chosen_line][chosen_row] is not 0:
            chosen_line = random.randint(0,5)
            chosen_row = random.randint(0,5)
        mapa[chosen_line][chosen_row] = 2





def display_mapa(mapa):
    i=0
    print('',0,1,2,3,4,5)
    for line in mapa:
        print(i,sep='',end='')
        i+=1
        for space in line:
            if space == 0:
                print('?',sep='',end=' ')
            if space == 1:
                print('?',sep='',end=' ')
            elif space == 2:
                print('?',sep='',end=' ')
            elif space == 3:
                print('X',sep='',end=' ')
            elif space >=4:
                print('J',sep='',end=' ')
        print('')
    print(f'')


def validar_movimento(mapa,pos,points,move):
    print(f'Movimento restante {move}')
    movimento = input('Qual direção deseja se movimentar\n W - para cima \n S para baixo\n A - para esquerda \n D - para direita')
    if movimento.upper() in 'WASD':
        #direção valida

        #checkar se fora do mapa
        if (movimento == 'W' and mapa[pos[0]] == 0):
            print('direção invalida, fora do mapa')
            return validar_movimento(mapa,pos,move)
        elif movimento == 'S' and mapa[pos[0]]== 5:
            print('direção invalida, fora do mapa')
            return validar_movimento(mapa,pos,move)
        elif movimento == 'A' and mapa[pos[1]]==0:
            print('direção invalida, fora do mapa')
            return validar_movimento(mapa,pos,move)
        elif movimento == 'D' and mapa[pos[1]]==5:
            print('direção invalida, fora do mapa')
            return validar_movimento(mapa,pos,move)
        movimentar(mapa,pos,points,move,movimento)
        
    else:
        print('Direção não reconhecida,por favor digite apenas (W A S D)')
        return validar_movimento(mapa,pos,move)
    
def movimentar(mapa,pos,points,move,movimento):
    mapa[pos[0]][pos[1]] =3 
    move -= 1
    if movimento == 'W':
        pos[0] -=1 
        reagir_posicao(mapa[pos[0]][pos[1]],points,move)
        mapa[pos[0]][pos[1]] =3
    elif movimento == 'S':
        pos[0] +=1 
        reagir_posicao(mapa[pos[0]][pos[1]],points,move)
        mapa[pos[0]][pos[1]] =3
    elif movimento == 'A':
        pos[1] -=1 
        reagir_posicao(mapa[pos[0]][pos[1]],points,move)
        mapa[pos[0]][pos[1]] =3
    elif movimento == 'D':
        pos[1] +=1 
        reagir_posicao(mapa[pos[0]][pos[1]],points,move)
        mapa[pos[0]][pos[1]] =3
    else:
        print('Erro Desconhecido')

points = 0
movimento = 10
inserir_tesouro(mapa,10)
inserir_armadilhas(mapa,5)
for row in mapa:
    print(row)

def reagir_posicao(num,points,move):
    if num == 0:
        print('Espaço Vázio')
    elif num == 1:
        print('Parabens,tesouro encontrado\n +500 points')
        points+=500
    elif num == 2:
        print('Que pena! caiu em armadilha, perdeu 3 Movimento \n -3 Move')
        move -=3
    else:
        print('espaço ja explorado')

while movimento >0:
    pos = [2,2]
    display_mapa(mapa)
    print(f'Points:{points}           ')
    validar_movimento(mapa,pos,points,movimento)
