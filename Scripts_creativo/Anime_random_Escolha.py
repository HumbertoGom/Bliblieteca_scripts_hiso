from Anime_random import episodios_dbc, episodios_DBZ,ranma_titulos,episodios_gt,episodios_DBS
import random

RANMA_173 = ranma_titulos



print(len(episodios_dbc))
print(len(episodios_DBZ))
print(len(episodios_gt))
print(len(episodios_DBS))

DB_344 = episodios_dbc + episodios_DBZ
DB_410 = DB_344 + episodios_gt
DB_475 = DB_344 + episodios_DBS
DB_539 = DB_410 + episodios_DBS

RANMA_161 = RANMA_173[:-12]

for ep in RANMA_161:
    print(ep)

OPÇÕES= [DB_344,DB_410,DB_475,DB_539,RANMA_173,RANMA_161]
if __name__ == '__main__':
    while True:
        print('[1] Dragon ball 344: clássico + Z')
        print('[2] Dragon ball 410: classico + Z +GT')
        print('[3] Dragon ball 475: classico + Z + Super')
        print('[4] Dragon ball 539: todos os 4 Dragon ball')
        print('[5] ranma 173:anime deen + OVAs')
        print('[6] ranma 161:anime deen sem OVAs')
        escolha = input('Escolha um conjunto para pegar anime aleatório')
        try:
            escolha = int(escolha)
        except:
            continue
        print('episódio escolhido: ')
        print(random.choice(OPÇÕES[escolha-1]))
        print('')