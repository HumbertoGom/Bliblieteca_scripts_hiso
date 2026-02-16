
from random import choice,randint,random,choices,uniform
from openpyxl import Workbook

#para os vendores, botei uns personagens aleatórios.
vendedores= ['Anna' ,'Camilla' ,'karla' ,'Nabiki' , 'Piano']
Peso_vendedores = [65,10,2,20,3] #claro que a anna vende mais que os outros,ela tem um secret shop em cada dimensão

#lista de compradores, maioria são axe fighters de fire emblem
compradores = ['Barst','Bord','Cord','Ward','Lot','Dorcas','Bartre','Garcia','Boyd','Nolan','Dice','Vaike','Arthur','Charlotte','Gazak','Edelgard','Claude','Caspar','Bernadetta','Dedue','Ashe','Raphael','Ignatz','Athos','Bartre','Canas','Dart','Dorcas','Eliwood','Erk','Farina','Fiora','Florina','Geitz','Guy','Harken','Hawkeye','Heath','Hector','Isadora','Jaffar','Karel','Karla','Kent','Legault','Louise','Lowen','Lucius','Lyn','Marcus','Matthew','Merlinus','Nils','Ninian','Nino','Oswin','Pent','Priscilla','Rath','Raven','Rebecca','Renault','Sain','Serra','Vaida','Wallace','Wil']

produtos = [{"iron bow": 300},{'Steel Lance':550},{"iron sword": 340},{"iron Axe":240},{"Steel Axe":360},{"Hand Axe":300},{"Silver Axe":700},{"Silver Sword": 960},{"Arms Scroll":5000},{"Pugi Axe":1500},{"Armads":8000}] # armas de fire emblem.
Peso_produtos = [10,8,15,30,20,50,8,4,2,15,2]
Peso_produtosV3 = [Peso_produtos[p] * uniform(0.5,1.5) for p in range(len(produtos))]

tipo_de_pagamento = ["Pix","Cartão","Boleto"]
peso_pagamento = [70,25,5]


wb= Workbook()
ws= wb.active
ws.title = 'Vendas_De_Axe_Sasune'
#print('Vendedor | Produto | Comprador | Preço | Pagemento \n' )
ws.append(['Vendedor','Produto','Comprador',"preço",'forma de pagamento']) # primeira linha

#loop cria uma linha de cada vez.
for row in range(100):
    produto = choices(produtos,weights= Peso_produtosV3,k=1)[0]  #produto como aleatório pesado
    nome_produto,preco = next(iter(produto.items()))             #separa nome do preço do produto
    row = [choices(vendedores,weights = Peso_vendedores,k=1)[0],nome_produto,choice(compradores),preco,choices(tipo_de_pagamento,weights=peso_pagamento,k=1)[0]]
    print(row)
#    print(f'{choice(vendedores)}   {nome_produto}   {choice(compradores)}   {preco}    {choice(tipo_de_pagamento)}')
    ws.append(row)

wb.save(r'c:\Users\sarge\OneDrive\Documentos\Base_de_DadosTesteV3.xlsx')