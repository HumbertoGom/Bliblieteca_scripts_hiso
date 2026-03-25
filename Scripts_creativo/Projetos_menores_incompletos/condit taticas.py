import random



#numero_formatado = numero[0:4]+'-'+ numero[3:7]

def cellnumb():
    numero = str(random.randint(10000000,99999999))
    return numero[0:4]+'-'+ numero[3:7]
lista_telefon ={
                
                'Roy': cellnumb() ,
                'Bors':cellnumb() ,
                'Allan':cellnumb(),
                'Marcus' :cellnumb(),
                'Rutger': cellnumb(),
                'Elen':cellnumb(),
                'Saul':cellnumb(),
                'Lot':cellnumb(),
                'Lilina':cellnumb(),
                'Fir':cellnumb(),
                'Broly':cellnumb(),
                'Zephiel':cellnumb}
for i in lista_telefon.keys():
    print (i)

while True:
    entrada = input('Saiba o nome de celular do seu personagem de fire emblem 6 favorito\n' 
    'digite apenas o nome dele ou dela')
    print (f'\no número de telefone do {entrada} é :',lista_telefon[entrada],'\n')