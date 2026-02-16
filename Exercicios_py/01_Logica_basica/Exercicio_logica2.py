

ordem1= [['tatewaki','3','Frango'],['ranma','2','Macarrão'],['Ukyo','2','aquela coisa']]

ordous = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]


print(f"{8}")
def orders(ordems):
    menu = []
    nums = []
    qtd_pedidos = {}
    for ordem in ordems:
        numero = ordem[1]
        pedido = ordem[2]
        menu.append(pedido)
        nums.append(int(numero))
        if qtd_pedidos.get(numero) == None:
            qtd_pedidos[numero] = [pedido]
        elif qtd_pedidos.get(numero) is not None:
            qtd_pedidos[numero].append(pedido)
   
    nums= set(nums)
    print('n1   ',nums)
    
    menu = set(menu)

 

    nums = sorted(nums)
    nums = set(str(x) for x in nums)

    print('n2   ', nums)
    print(qtd_pedidos)
    expr = []

    menu = list(menu)
    menu.insert(0,'Table')
    expr.append(menu)
 #   expr = ['Table']
 #   for i in menu:
  #      expr.append(i) # expr = primeira linha

    for num in nums:
        pedido_mesa = []
        pedido_mesa.append(num)
        for item in menu:
            if item == 'Table':
                continue
            elif item in qtd_pedidos[num]:
                pedido_mesa.append(1)
            elif item not in qtd_pedidos[num]:
                pedido_mesa.append(0)
        expr.append(pedido_mesa)
    print('expr: //',expr)
    return expr
 #   print(nums)
 #   print(menu)


#orders(ordem1)
orders(ordous)