# EXERCICIO 1 DA AULA 54 DO CRUSO
inteiro = input('Digite um numero inteiro')
try:
    inteiro = int(inteiro)
    if inteiro % 2==0:
        print(f'{inteiro} é um número par')
    else:
        print(f'{inteiro} é um número impar')
except:
    print(f'{inteiro} não é um número inteiro')