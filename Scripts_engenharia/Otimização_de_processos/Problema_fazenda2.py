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
Scf = np.array([   [101,102,103],   #Área selecionada para cada cultura
                   [101,300,103],
                   [101,102,103]])

Ycf = np.array([[ True,False,True],   #binária, quais culturas haveram em cada fazenda
                [ True,False,True],
                [ True,False,True]])

print ((Lc*Scf).sum())
def Fobj(x):
    Ycf_flat = x[:9] #descompactação de var
    Scf_flat = x[9:]
    Ycf = Ycf_flat.reshape(3,3)
    Scf = Scf_flat.reshape(3,3)
    
    #calculo do ganho
    ganho = (Lc*Scf).sum() # cria uma matriz com o lucro bruto de cada terreno e soma cada elemento.

    #calculo do custo
    custo = 5000 * Ycf.sum() # soma 1 para cada plantação existente,depois multiplica por 5000

    lucro = ganho - custo
    return -lucro  # -lucro, pq optimize apenas minimiza


# compactação da variável
x0 = np.concatenate([Ycf.ravel(), Scf.ravel()])
Fobj(x0)

'''
sol = optimize.minimize(Fobj, x0, method='L-BFGS-B')


x_opt = -sol.x               # vetor 1D

n = Ycf.size                # nº elementos da primeira matriz
Ycf_opt = x_opt[:n].reshape(Ycf.shape)
Scf_opt = x_opt[n:].reshape(Scf.shape)

print("Ycf otimizado:\n", Ycf_opt)
print("Scf otimizado:\n", Scf_opt)
'''
