entrada = input('digite uma palavra' )
frequencia = {}
for letra in entrada:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] =1 
print (frequencia)