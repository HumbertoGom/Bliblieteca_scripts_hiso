
alunos ={
    'Akane':7,
    'Ranma':6,
    'Tatewaki':2,
    'Ukyo':8,
    'Kiba I': 2
}

result = {}
for chave,valor in alunos.items():
    if valor in result:
        result[valor].append(chave)
    else:
        result[valor] = [chave]

print (result)
