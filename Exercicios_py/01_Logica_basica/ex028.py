#dicionario de dicioanrios.
cidades = {
    'Oldale' :{'população': 8001, 'temperatura': 300},
    'Dewford' :{'população': 1021, 'temperatura': 295}
}




#print(cidades['Dewford']['população'])

#print(cidades['Oldale']['população'])


while True:
    print('\n\nbem vindo a previsão do tempo de hoenn,\n estamos falidos,porque nossa reporter apostou o orcamento do programa\n,então só temos dados de duas cidades\n [Oldale] ou[Dewford] ')
    entrada = input('qual cidade voçê quer ver a tempo?')
    print (entrada)
    cidade = cidades[entrada]
    print(f'a temperatura em {entrada} é ',sep='')
    print(cidade['temperatura'],'K,isso são ',cidade['temperatura']-273, 'em celcius')
#'{cidades[entrada]['temperatura'] - 273}