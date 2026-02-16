
gaming = {'n-word': 2000,
            'F-word': 3000}

moving = {'s-word': 9000,
            'F-word':1000}



resultado = gaming.copy()

for chave,valor in moving.items():
    if chave in resultado:
        resultado[chave] += valor
    else:
        resultado[chave] = valor

print (resultado)