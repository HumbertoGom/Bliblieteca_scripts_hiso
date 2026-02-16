#exercicio 2 da aula 54
hora=input('Que horas são? ')
minuto=input('quantos minutos ')
try:
    hora=int(hora)
except:
    print('digite uma hora válida e inteira')
if hora >=0 and hora<=11:
    print('bom dia')
elif hora>=12 and hora<=17:
    print('boa tarde ')
elif hora>=18 and hora<=23:
    print('boa noite')
else:
    print('digite uma hora valida')
print(f'são {hora}:{minuto}')