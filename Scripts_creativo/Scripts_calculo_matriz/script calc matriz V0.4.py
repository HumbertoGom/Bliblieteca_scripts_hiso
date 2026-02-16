import numpy as np



def criar_matriz():
    # Passo 1: Pedir ao usuário o número de linhas e colunas
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    # Passo 2: Criar uma matriz nula (de zeros)
    matriz = np.zeros((linhas, colunas))

    print('como deseja preencher a Matriz?')
    print('[I]nserindo cada valor,[P]reenchendo com um único número?,[M]atriz Idendidade,[A]leatorio preenchimento')
    
    entrada = (input(' '))
# Passo 3: Preencher a matriz com valores fornecidos pelo usuário
    if entrada == 'I':
        for i in range(linhas):
            for j in range(colunas):
                matriz[i, j] = float(input(f"Digite o valor para a posição ({i}, {j}): "))
    elif entrada == 'P':
        print('criando matriz Preenchida, digite o valor de todos os elementos')
        entrada = input(' ')
        matriz = np.full((linhas,colunas), entrada)
    elif entrada == 'M':
        print('Criando matriz identidade')
        matriz = np.eye(linhas,colunas)
    elif entrada == 'A':
        print('Criando Matriz aleatória')
        matriz = np.random.rand(linhas,colunas)
    else:
        print('valor não reconhecido, retornando matriz nula ')

    # Passo 4: Exibir a matriz final
    print("\nMatriz final:")
    return matriz

m0= criar_matriz()
m1=  None
m2=  None
m3=  None
m4=  None
m5=  None


def tranposta(m):
    return m.T

def listar_memoria():
    print(f'Espaço 0: {m0}')
    print(f'Espaço 1: {m1}')
    print(f'Espaço 2: {m2}')
    print(f'Espaço 3: {m3}')
    print(f'Espaço 4: {m4}')    
    print(f'Espaço 5: {m5}')



#melhor nao usar essa função,deve criar problemas de escopo
def sobreescrever():
    print('Voçê escolheu Copiar, para qual espaço vai copiar a Matriz Atual?')
    listar_memoria()
    entrada = input('Qual o espaço a ser sobrescrito?')
    if entrada.isnumeric():
        entrada = int(entrada)
        if entrada <6 and entrada >=0:
            if entrada == 0:
                m0 = matriz_atual
            if entrada == 1:
                 m1 = matriz_atual
            if entrada == 2:
                m2 = matriz_atual
            if entrada == 3:
                m3 = matriz_atual    
            if entrada == 4:
                m4 = matriz_atual
            if entrada == 5:
                m5 = matriz_atual
        else:
                print('o número escolhido Não esta no intervalo ')
    else:
        print ('Por favor digite números inteiros ')


def op_simples(matriz):
    print('Escolha uma operação simples')
    print('[S]oma escalar: soma cada elemento da matriz por um valor')
    print('[P]roduto escalar: multiplica cada elemento da matriz por um escalar')
    print('[T]raço:calucla o Traço da matriz')
    print('[D]eterminante: Calcula o determinate da matriz')
    print('[I]nversão: retorna a matriz inversa')
    print(f'a matriz selecionada atual é \n{matriz}\n')
    entrada = input('')
    if entrada == 'S':
        entrada = input('Digite um número para somar a cada membro da matriz')
        if entrada.isnumeric():
            matriz+= int(entrada)
        print(matriz)
    elif entrada == 'P':
        entrada = input('Digite um número para Multiplicar a cada membro da matriz')
        if entrada.isnumeric():
            matriz*= int(entrada)
        print(matriz)
    elif entrada == 'T':
        traco = np.trace(matriz)
        print(f' o traço da matriz: \n{matriz}\n é {traco}')
    elif entrada == 'D':
        determinante = np.linalg.det(matriz)
        print(f'o Determinante da matriz: \n{matriz}\n é {determinante}')
    elif entrada == 'I':
        matriz = np.linalg.inv(matriz)
        print(matriz)
    return matriz

def op_complexas(matriz,matriz_operante):
    print('Escolha uma Operação, [S]oma matricial ou [M]ultiplicação de matrizes')
    entrada = input('')
    if entrada == 'S':
        print(f'{matriz} + {matriz_operante} ')
        matriz = matriz + matriz_operante
        print(matriz)
        return matriz
    elif entrada  == 'M':
        print(f'{matriz} vezes {matriz_operante}')
        matriz = matriz @ matriz_operante 
        print(matriz)
        return matriz       

def escalonamento(matriz):
    linhas,colunas = matriz.shape
    for i in range(linhas):
        pivo = matriz(i,i)
        


matriz_atual = m0

while True:
    print('A matriz selecionada atual é\n')
    print(matriz_atual)
    print('que operação fazer? ')
    print('[C]ópiar, [T]ranspor, [M]ontar,[O]perações,[S]elecionar')
    entrada = (input('Escolha uma Opção \n\n'))
    if entrada == 'C':
# 'C' é a operação que chamei copiar, mas na verdade,reescreve uma das 5 variáveis, para guardar a Matriz selecionada
        print('Voçê escolheu Copiar, para qual espaço vai copiar a Matriz Atual?')
        print(f'Espaço 0: {m0}')
        print(f'Espaço 1: {m1}')
        print(f'Espaço 2: {m2}')
        print(f'Espaço 3: {m3}')
        print(f'Espaço 4: {m4}')    
        print(f'Espaço 5: {m5}')
        entrada = input('Qual o espaço a ser sobrescrito?')
        if entrada.isnumeric():
            entrada = int(entrada)
            if entrada <6 and entrada >=0:
                if entrada == 0:
                    m0 = matriz_atual
                if entrada == 1:
                    m1 = matriz_atual
                if entrada == 2:
                    m2 = matriz_atual
                if entrada == 3:
                    m3 = matriz_atual    
                if entrada == 4:
                    m4 = matriz_atual
                if entrada == 5:
                    m5 = matriz_atual
            else:
                print('o número escolhido Não esta no intervalo ')
        else:
            print ('Por favor digite números inteiros ')
    if entrada == 'T':
#'T' é uma simples tranposição
        matriz_atual= tranposta(matriz_atual)
        print('A matriz foi transposta')
    if entrada == 'M':
#'M' retorna pro começo do código na função Criar_Matriz(), 
# chatGPT me ajudou com essa
        matriz_atual = criar_matriz()
    if entrada == 'S':
#'S' Cópia uma das 6 matrizes guardadas nas variáveis, para matriz selecionada atual
        print('Mudar a Matriz selecionada para uma que foi salva na memória ')
        print('escolha uma matriz da memória, para copia a seleção ')
        print(f'Espaço 0: {m0}')
        print(f'Espaço 1: {m1}')
        print(f'Espaço 2: {m2}')
        print(f'Espaço 3: {m3}')
        print(f'Espaço 4: {m4}')    
        print(f'Espaço 5: {m5}')
        entrada = input('Digte qual espaço selecionar ')
        if entrada.isnumeric(): 
            entrada = int(entrada)
            if entrada <6 and entrada >=0:
                if entrada == 0:
                    matriz_atual = m0
                if entrada == 1:
                    matriz_atual = m1
                if entrada == 2:
                    matriz_atual = m2
                if entrada == 3:
                    matriz_atual = m3    
                if entrada == 4:
                    matriz_atual = m4
                if entrada == 5:
                    matriz_atual = m5
            else:
                print('o numero escolhido não esta no intervalo ')
        else:
            print('valor não número digitado em (Selecionar) recomeçando ')
    if entrada == 'O':
        print('as operações são divididas em:')
        print('Operações [S]imples: que envolvem apenas uma matriz')
        print('Operações [C]omplexas: envolvem duas matrizes,como multipliação de matrizes')
        entrada = input('Escolha um tipo de operação\n\n')
        if entrada == 'S':
            matriz_atual = op_simples(matriz_atual)
        if entrada == 'C':
            print(f'operações complexas requerem duas matrizes, \n{matriz_atual}\n sofrerá alteração de?')
            listar_memoria()
            entrada = input('Escolha a matriz Operante')
            if entrada.isnumeric == False:
                print('entrada não numerica')
                continue
            entrada = int(entrada)
            if entrada <6 and entrada >=0:
                if entrada == 0:
                    matriz_operante = m0
                if entrada == 1:
                    matriz_operante = m1
                if entrada == 2:
                    matriz_operante = m2
                if entrada == 3:
                    matriz_operante = m3    
                if entrada == 4:
                    matriz_operante = m4
                if entrada == 5:
                    matriz_operante = m5
            else:
                print('o numero escolhido não esta no intervalo ')
                continue
            matriz_atual = op_complexas(matriz_atual,matriz_operante)