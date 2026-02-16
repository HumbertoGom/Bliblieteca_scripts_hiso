#sistema de aluno online do colegio furikan

alunos ={
    'Akane':[6,7,2],
    'Ranma':[8,4,2],
    'Tatewaki':[2,0,0],
    'Ukyo':[9,8,2]
}

medias =[]

def media_esp(notas):
    cont =0
    for j in notas:
        cont +=j
    return (cont/2.2)


for i,j in alunos.items():
    print(f'a média de {i} é {media_esp(j):.2f}')

