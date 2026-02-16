import json


class unidade:
    def __init__(self,nome,SKL,SPD,HP,DEFEN):
        self.nome = nome
        self.skl = SKL
        self.spd = SPD
        self.hp = HP
        self.defen = DEFEN

print()
gordin = unidade('gordin,',3,1,21,2)
arran = unidade('arran',8,5,35,8)
navarre = unidade('navarre',6,12,23,3)
draug = unidade('draug',4,3,25,9)
print(vars(draug))

player = [gordin,arran,navarre,draug]

with open('exercicio024.json','w',encoding='utf-8') as arquivo:
    for i in player:
        json.dump(vars(i),arquivo,indent=2,ensure_ascii= False)

