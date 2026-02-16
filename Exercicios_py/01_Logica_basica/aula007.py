nome = input('digite seu nome')
idade = input('digite sua idade')
if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome inveritdo é {nome[::-1]}')
    if ' ' in nome:
        print ('seu nome contem espaços')
    else:
        print('seu nome não contem espaços')
    print(f'seu nome contem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a últimaletra do seu nome é {nome[-1]}')
else:  
    print('Desculpe,voçê deixou campos vazios')
input('esse foi o resultado')