'''
Enunciado: 

Uma cooperativa agrícola opera 3 fazendas que possuem produtividades aproximadamente iguais entre si. A produção total por fazenda depende fundamentalmente da área disponível para o plantio e da água de irrigação.  

A cooperativa procura diversificar sua produção de modo que vai plantar este ano três tipos de cultura em cada fazenda a saber: milho, arroz e feijão. Cada tipo de cultura demanda por uma certa quantidade de água. Para reduzir o conflito no uso das colheitadeiras, que são alugadas pela cooperativa, estabeleceram-se limites de área de produção dentro de cada tipo de cultura. 

Para evitar a concorrência entre os cooperados, acordou-se que a proporção de área cultivada seja a mesma para cada uma das fazendas. As tabelas a seguir resumem os dados tecnológicos: 
'''

import numpy as np
from scipy import optimize

#Indices
F= [0,1,2] #0 - fazenda 1, 1 - fazenda 2, 2 - fazenda 3
C= [0,1,2] #0 - Milho, 1 - Arroz, 2 - Feijão

#Parâmetros

Af = [400,650,350] #area disponivel para cada fazenda(acres)
Wf = [1800,2200,950] # água disponível p cada fazaenda (L)

Ac = [660,880,400] #área máxima(acre)
Kc = [5.5,4,3.5] #Consumo de água p cada cultura(L/acre)
Lc = [5000,4000,1800] #Lucro de cada cultura(R$/acre)

# variaveis

#                    M   A   F
Scf = np.array([   [151,240,1],   #Área selecionada para cada cultura
                   [7,530,7],
                   [0,214,5]])

Ycf = np.array([[ True,True,True],   #binária, quais culturas haveram em cada fazenda
                [ True,True,True],
                [ True,True,True]])




# lucro das cultura
#GANHO
def Fobj(x):      # X é a as duas variáveis comprimidas
    # descompactanto os vetores
    #  primeiros 9 são Ycf, últimos 9 são Scf
    Ycf_flat = x[:9]
    Scf_flat = x[9:]
    
    Ycf = Ycf_flat.reshape(3,3)
    Scf = Scf_flat.reshape(3,3)
    #Calculo do GANHO
    ganho = 0 
    milho = arroz = feijão = 0
    for f in Scf:     #aqui estou somando as áreas de cada cultura
        milho += f[0]
        arroz += f[1]
        feijão += f[2] 
    culturas = [milho,arroz,feijão]   
    for i in range(3):
        ganho += Lc[i]* culturas[i]
    
    #calculo do PREIJUIZO
    preijuizo = 0
    for c in Ycf:
        for f in c:
            preijuizo += f * 5000

    lucro = ganho - preijuizo 
    return 1/lucro     #estou invertendo o lucro pq, comando optimize apenas otimiza minimização de funções

x0 = np.concatenate([Ycf.ravel(), Scf.ravel()])

print(f'função objetivo resultado:{1/Fobj(x0)}')

'''
Solucao = optimize.minimize(Fobj,x0, method='L-BFGS-B')
print (Solucao)

x_opt = Solucao.x  # vetor 1D com todos os valores

n = Ycf.size                # nº elementos da primeira matriz
Ycf_opt = x_opt[:n].reshape(Ycf.shape)
Scf_opt = x_opt[n:].reshape(Scf.shape)

print("Ycf otimizado:\n", Ycf_opt)
print("Scf otimizado:\n", Scf_opt)

COMPARAÇÃO ENTRE MODELOS: os dois eram iguais
sugest2 = 0
sugest2 += Scf * Lc

Sugest1=0
for f in Scf:
    Sugest1 += (Lc * f

sugest2= sugest2.sum()
Sugest1= Sugest1.sum()
print(f'sugestão 1 {Sugest1}\nsugestão 2 {sugest2}')


'''