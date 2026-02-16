
 # Exercício - Unir listas
 # Crie uma função zipper (como o zipper de roupas)
 # O trabalho dessa função será unir duas
 # listas na ordem.
 # Use todos os valores da menor lista.
 # Ex.:
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
 # Resultado
 # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def unir_listas(l1,l2):
    lista_final = []
    for i in l1:
        icount =0
        for j in l2:
            jcount=0
            if l1[icount] == l2[jcount]:
                lista_final.append(set(i,j))
            jcount+=1
        icount+=1
    return lista_final
print (unir_listas(lista1,lista2))