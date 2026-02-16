ordem1= [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

ordem2 = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]

def tabelar(pedidos):
    #tratamento dos dados
    pedidosmesa = {}
    mesas =  set()
    comidas = set()

    for pedido in pedidos:
        #coletar valores do dado original
        numeroA= int(pedido[1])
        comidaA= pedido[2]
        # adicionar aos indices
        mesas.add(numeroA)
        comidas.add(comidaA)
        #criar o dicionario que liga mesa a comida
        if pedidosmesa.get(numeroA) == None:
            pedidosmesa[numeroA] = [comidaA]
        elif pedidosmesa.get(numeroA) is not None:
            pedidosmesa[numeroA].append(comidaA)


    #organizar indieces
    mesas = sorted(mesas)
    comidas = sorted(comidas)


    #organizar dict
    tempdict = {}
    for chave in mesas:
        tempdict[chave] = pedidosmesa[chave]
    pedidosmesa = tempdict


    print('pedidosmesa ', pedidosmesa)
    comidas.insert(0,'Table')
    print('comidas ',comidas)
    print('mesas ',mesas) 
    #criar expressão
    expr = []
    expr.append(comidas)
    for mesa in mesas:
        pedidoA = []
        for comida in comidas:
            if comida == 'Table':
                pedidoA.append(str(mesa))
            if comida in pedidosmesa[mesa]:
                pedidoA.append(str(pedidosmesa[mesa].count(comida)))
            elif comida not in pedidosmesa[mesa] and comida != 'Table':
                pedidoA.append('0')
        expr.append(pedidoA)
    print(expr)
    return expr    







tabelar(ordem2)