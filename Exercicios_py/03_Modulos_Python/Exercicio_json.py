import json

CAMINHO_ARQ= 'dados_exercicio.json'
def ler(caminho_arq):
    dados = []
    with open(caminho_arq, 'r',encoding='utf-8')as arquivo:
        dados = json.load(arquivo)
tarefas = []
excluido =[]
while True:
    print('Comandos: listar, desfazer, refazer ')
    entrada = input('Digite uma tarefa ou commando ')
    if entrada == 'listar':
        print (tarefas)
    elif entrada =='desfazer':
        excluido.append(tarefas[-1])
        tarefas.pop()
    elif entrada == 'refazer':
        tarefas.append(excluido[-1])
        excluido.pop()
    else:
        tarefas.append(entrada)
    with open('dados_exercicio.json','w',encoding='utf-8')as arquivo:
        json.dump(tarefas,arquivo)

