primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')


int_primval=int(primeiro_valor)
int_secval=int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior do que {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor} é maior do que {primeiro_valor} ')
else:
    print(f'{primeiro_valor} é igual a {segundo_valor}')