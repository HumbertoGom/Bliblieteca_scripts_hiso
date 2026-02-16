#calculadora while
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite Outro número: ')
    operador = input('escolha uma operação [+][-][/][*]')
    num_validos = None
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('um ou ambos os números são inválidos')
        continue
    resultado = 0
    if operador == '+':
        resultado = numero_1 + numero_2
    elif operador == '-':
        resultado = numero_1 - numero_2
    elif operador == '/':
        resultado = numero_1 / numero_2
    elif operador == '*':
        resultado = numero_1 * numero_2
    else:
        print('digite um operador válido ')
        continue
    print(resultado)

    sair= input('Quer sair? [s]im:')
    sair = sair.lower()
    sair = sair.startswith('s')
    if sair:
        break