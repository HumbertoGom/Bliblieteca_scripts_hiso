"""exercicio #3 da aual 54"""
nome=input('Digite seu nome')
tamanho=len(nome)
print (tamanho)
if tamanho <=4:
    print('Seu nome é curto')
elif tamanho == 5 or tamanho == 6:
    print('seu nome é normal')
else:
    print('Seu nome é muito grande')