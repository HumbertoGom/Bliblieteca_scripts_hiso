CPF = '746.824.890-70'
contador_regressivo1=10
soma = 0
for i in CPF:
    try:
        print(i,contador_regressivo1)
        i=int(i)
        if i==0 or contador_regressivo1==0:
            continue
        soma += i * contador_regressivo1
        contador_regressivo1 = contador_regressivo1- 1
        print(i,contador_regressivo1)
        if contador_regressivo1 == 2:
            break
    except:
        continue
print(soma)
soma *= 10
digito1= soma % 11
digito1 = digito1 if digito1<= 9 else 0
print('o primeeiro digito do CPF deve ser:')
print(digito1)
contador_regressivo2 = 11
soma2=0
for j in CPF:
    try:
        j=int(j)
        print(j,contador_regressivo2)
        if j == 2:
            soma2+=(j * digito1)
            break
        soma2 += (j *  contador_regressivo2)
        contador_regressivo2 -=1


    except:
        continue
print (soma2)
digito2= (soma2*10)%11
digito2 = digito2 if digito2<= 9 else 0
print(digito2)
