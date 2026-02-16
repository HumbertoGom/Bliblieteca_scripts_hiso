
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador =1
for i in range(3):
    pergunta = perguntas[i]
    print (pergunta['Pergunta'])
    for j in (pergunta['Opções']):      
        print(f'{contador}) {j}')
        contador +=1
    resposta = input('Digite a resposta')
    try:
        resposta = int(resposta)
    except ValueError:
        print('resposta invalida ')
        continue
    correta = int(pergunta['Resposta'])
    print(correta)
    if resposta == correta:
        print(f'Voçê acertou, a resposta era {correta} ')
    else:
        print(f'Voçê errou, a resposta era {correta} ')
    