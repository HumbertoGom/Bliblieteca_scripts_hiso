import random
#ez

vogais =['a','e','i','o','u']
def contar_vogais(pal):
    contagem=0
    for letra in pal:
        if letra in vogais:
            contagem+=1
    print(contagem)
contar_vogais('aaaeeeiii')


def maior_numero():
    nums=set()
    for i in range(5):
        i=int(input(f'Digite um número ({i+1})'))
        nums.add(i)
    for n in nums:
        cont_maior=0
        for n2 in nums:
            if n >= n2:
                cont_maior+=1
        if cont_maior == len(nums):
            print(n)

def palindromo(palavra):
    palavrainv = ''
    i=-1
    for letra in palavra:
        palavrainv+=palavra[i]
        i-=1
    if palavrainv == palavra:
        print(f'{palavrainv} é um palindromo ') 
    else:
        print(f'{palavra} não é um palindrômo ')
print('\n\n')

def soma_impar_par(n):
    pares=0
    impares=0
    for num in range(n+1):
        if num%2==0:
            pares+=num
        else:
            impares+=num
    print(f'soma dos pares {pares}\n soma dos impares {impares}')

def tabuada():
    n=int(input('Digite um numero para ver sua tabuada '))
    for i in range(10):
        print(f' {n} x {i+1}  = {n* (i+1)}')


#medios

def fibonacci(n):
    fib=[0,1]
    for i in range(n):
        print(i)
        if i == 0 or i==1:
            print('não somado')
        else:
            fib.append(fib[-1]+fib[-2])
    print(fib)

def caixa_elec(D):
    D0=D
    nota_100 = D//100
    D-= nota_100 * 100
    nota_50 = D//50
    D-= nota_50 * 50 
    nota_20 = D//20
    D-= nota_20 * 20 
    nota_10 = D//10
    D-= nota_10 * 10 
    nota_5 = D//5
    D-= nota_5 * 5 
    nota_2 = D//2 
    D-= nota_2 * 2
    print(f'{D0} pode ser em dividido em \n{nota_100} x 100,00R$   \n{nota_50} x 50,00R$\n{nota_20} x 20,00R$\n{nota_10} x 10,00R$\n{nota_5} x 5,00R$\n{nota_2} x 2,00R$')

def primo(n):
    zero_count=0
    for i in range(n):
        if n%(i+1) == 0:
            zero_count +=1
    if zero_count == 2:
        print(n,' é um número primo')
    else:
        print(n, ' não é um número primo')



def impar_par():
    entrada = input('Escolhe [P]ar ou [I]mpar?')
    numero_esc = int(input('escolha um número '))
    numero_maq = random.randint(0,10)
    resultado = numero_maq+numero_esc 
    print(f'CPU jogou {numero_maq}')
    print('\n')
    print(f'{numero_esc}+{numero_maq} = {resultado}')

    if entrada.upper() == 'P':
        print('Maquina fica com Impar')
        if resultado%2 == 0:
            print('parabens voçê ganhou')
        else:
            print('voçê perdeu')


    elif entrada.upper() == 'I':
        print('Maquina fica com Par')

        if resultado%2 == 0:
            print('voçê perdeu')        
        else:
            print('parabens voçê ganhou')


#hardo

def forca(secreta):
    resolvido = False
    display= '_' * len(secreta)
    while resolvido == False:
        print('forca: ', display)
        letra_ad= input('digite uma letra')
        i=0
        for letra in secreta:
            if letra == letra_ad:
                print(display[i])
            i+=1

forca('Naruto')
