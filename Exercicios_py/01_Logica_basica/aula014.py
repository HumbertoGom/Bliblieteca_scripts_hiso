lista = []

while True:

    entrada = input('Selecione uma Opção , [i]nserir [a]pagar [l]istar')
    if entrada == 'i':
        valor= input('Valor: ')
        lista.append(valor)
    elif entrada == 'a':
        apagar = input('qual indice a ser apagado')
        try:
            apagar = int(apagar)
            del(lista[apagar])
        except:
            print('näo foi possível apagar esse indice')
    elif entrada == 'l':
        for i in (enumerate(lista)):
            print (i)
    else:
        print('escolha uma opção válida')
