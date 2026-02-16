#cexercicio carro motor fabricante
class carro:
    def __init__(self,nome,motor,fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

class motor:
    def __init__(self,nome):
        self.nome = nome

class fabricante:
    def __init__(self,nome):
        self.nome = nome        



v8= motor('v8')
v9= motor('v9')
vbat = motor('vbat')

ford= fabricante('ford')
honda = fabricante('honda')
batmann = fabricante('alfred')

fusca = carro('fusca',v8,ford)
jipe = carro('jipe',v9,honda)
carro_do_ovo = carro('carro do ovo',v9,ford)
batmovel = carro('batmovel', vbat,batmann)

garagem = [fusca, jipe,carro_do_ovo,batmovel]

for i in garagem:
    print(i.nome +' '+ i.fabricante.nome +' '+ i.motor.nome,sep=' ')