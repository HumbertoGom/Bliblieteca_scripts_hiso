from colorama import Fore, Style, init
init(autoreset=True)
mapsize =(8,8)


# 0 - planicie, #1 montanha, #2 forest, #3 bridge, #4 castelo, #5 rio

composicao_do_mapa = [[1,1,1,1,1,5,1,1],
                      [1,1,1,1,5,5,1,0],
                      [0,4,1,0,3,0,0,0],
                      [0,0,0,0,5,0,0,0],
                      [0,0,0,0,5,0,0,0],
                      [0,0,0,0,5,0,0,0],
                      [0,2,2,0,5,0,0,0],
                      [2,2,2,2,5,0,0,5]
                        ]

personagem = [1,3]

def impri_quad(linha,coluna,j,personagem):
    if [linha,coluna] == personagem:
        print(Fore.RED+ 'A',end='')
    if j == 0:
        print(Fore.GREEN + "■",end='')
    if j==1:
        print(Fore.BLACK +'■',end='')
    if j==2:
        print(Fore.CYAN +'■',end='')
    if j==3:
        print(Fore.MAGENTA +'■',end='')
    if j==4:
        print(Fore.LIGHTYELLOW_EX +'■',end='')
    if j==5:
        print(Fore.BLUE +'■',end='')

def mostrar_mapa(mapa,personagem):
    for linha in range(len(mapa)):
        for coluna in range (len(mapa[linha])):
            impri_quad(linha,coluna,mapa[linha][coluna], personagem)

while True:
    mostrar_mapa(composicao_do_mapa,personagem)
    comando = input("Mover (w/a/s/d), ou 'q' para sair: ")
    if comando == 'q':
        break
    elif comando == 'w' and personagem[0] > 0:
        personagem[0] -= 1
    elif comando == 's' and personagem[0] < mapsize[0] - 1:
        personagem[0] += 1
    elif comando == 'a' and personagem[1] > 0:
        personagem[1] -= 1
    elif comando == 'd' and personagem[1] < mapsize[1] - 1:
        personagem[1] += 1