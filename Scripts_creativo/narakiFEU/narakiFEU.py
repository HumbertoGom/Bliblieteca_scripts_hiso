#naraki fire emblem unit

from pathlib import Path
import json

#estarei escrevendo o arquivo cópia,não quero perder minha obra prima de código
CHAR_L_DATA = r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\narakiFEU\Fire emblem stat model + ranma12 charcter.json"

CHAR_R_DATA = r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\narakiFEU\Fire emblem stat model + ranma12 charcter copy.json"




#sistema de escolha

def escolher():
    print(names_list)
    escolha = input('Digite o nome da unidade ') #usario deve escolher um dos nomes que vê.
#escolha = 'kasumi'  #vou debuggar com a linda da kasumi
#validação do sistema de escolha, ignora capitalização
    if escolha.lower() in namesLower:
        print(escolha)
    else: 
        print('digite nome válido ')    
    escolha = escolha.capitalize()
    return escolha

# essa função recebe nome escolhido, e retorna dicionario de unidade com "Name" correspondente
def choice_to_unitdict(choice):
    for unit_dict in unit_dict_list:
        if unit_dict["Name"].capitalize() == choice:
            return unit_dict    
    
    raise Exception(f'o nome escolhido "{choice}" não corresponde ao nome de nenhuma unidade no .json em{CHAR_R_DATA}\n lista dos nomes: {names_list}')

def edit_unit():
    unit_dict = choice_to_unitdict(escolher())
    print('escolha um atributo da unit para alterar: ')
    for stat,value in unit_dict.items():
        print(stat,':',value)


    #coletar stat escolhida
    stat_escolhida = input('Digite qual stat deseja alterar')

    if stat_escolhida in unit_dict.keys():
        print(f'alterando stat {stat_escolhida}')
        print(f'valor atual {unit_dict[stat_escolhida]}')

        if 'Growth' in stat_escolhida: # se for float
            print('alterando Growth Rate')
            valor_escolhido =  float(input('digite novo valor númerico para stat selecionada '))
        elif stat_escolhida == 'Name' or 'Class' or 'Unit Description': # se for alterar str
            if stat_escolhida == "Name":
                print('não vai dar certo alterar "Name",eu não programei direito,e mudar o código a estrutrua de dados daria muito trabalho\n isso acontece pq na hora de editar,eu verifico com o name, e se mudar o name,não da para editar ')
            valor_escolhido =  input('digite novo texto para stat selecionada ')
        else:
            valor_escolhido =  int(input('digite novo valor númerico para stat selecionada '))
        
        unit_dict[stat_escolhida] = valor_escolhido
        #altera o valor na temporária unit dict


        with open(CHAR_R_DATA,'r',encoding="utf-8") as arquivo: #carrega arquivo e reescreve na variavel chars
            chars = json.load(arquivo)
            for unit_in_file in chars.items():
                if unit_in_file[1]["Name"] == unit_dict["Name"]:
                   unit_in_file[1][stat_escolhida] = valor_escolhido
        with open(CHAR_R_DATA,'w',encoding="utf-8") as arquivo:
            json.dump(chars,arquivo, ensure_ascii=False, indent=4)                
    else:
        print('stat invalida escolhida')    

def Copiar_unit():
    print(names_list)
    copiar = input('Qual unidade deseja copiar?')
    if copiar.lower() in namesLower: #verificar com lower para não importa capitalização
        novo_unitdict = choice_to_unitdict(copiar.capitalize())
        novo_name = novo_unitdict["Name"] + " Copy"
        novo_unitdict["Name"] += ' Copy'

        with open(CHAR_R_DATA,'r',encoding="utf-8") as arquivo: #carrega arquivo e reescreve na variavel chars
            chars = json.load(arquivo)
            chars[novo_name] = novo_unitdict

        with open(CHAR_R_DATA,'w',encoding="utf-8") as arquivo:
            json.dump(chars,arquivo, ensure_ascii=False, indent=4)  
    else:
        print('nome invalido escolhido para copiar')

def display_stats():
    unit_dict = choice_to_unitdict(escolher())
    for stat,value in unit_dict.items():
        print(stat,':',value)

#edit_unit(choice_to_unitdict(escolha))

def criar_unit_dozero():
    nome = input('Digite nome da nova Unidade')
    novo_UD = dict()
    for stat,value in unit_dict_list[0].items():
        print(stat)
        if 'Growth' in stat: # se for float
             novo_UD[stat] = float(input(f'Digite um valor float para a stat {stat}'))
        elif stat in ('Name' , 'Class', 'Unit Description'):
            novo_UD[stat] = input(f'Digite um texto para a stat {stat}')
        else:
            novo_UD[stat] = int(input(f'Digite um Inteiro para a stat {stat}'))

    with open(CHAR_R_DATA,'r',encoding="utf-8") as arquivo: #carrega arquivo e reescreve na variavel chars
            chars = json.load(arquivo)
            chars[nome] = novo_UD

    with open(CHAR_R_DATA,'w',encoding="utf-8") as arquivo:
        json.dump(chars,arquivo, ensure_ascii=False, indent=4)  


def NarakiFEU():
    print('Naraiki FEU V1.0.0\n')
    print('o que deseja fazer')
    print('Unidades disponíveis:',*names_list,sep=',')
    print('qual ')
    entrada= input('[E]ditar stat de Unidade,[C]opiar unidade,[L]er stats de unidade,[M]ontar unidade. \n')
    entrada = entrada.upper()
    if len(entrada) >= 1:
        print('resposta grande demais,apenas uma letra')
    if entrada == 'E':
        edit_unit()
    elif entrada == 'C':
        Copiar_unit()
    elif entrada == 'L':
        display_stats()
    elif entrada == 'M':
        criar_unit_dozero()
    else:
        print(f'commando não reconhecido ({entrada})')

while True:
    with open(CHAR_R_DATA,'r',encoding="utf-8") as arquivo:
        chars = json.load(arquivo)

    unit_dict_list = [unit[1] for unit in chars.items()]
    names_list = [] #criando lista de nomes
    for unit in unit_dict_list:
        names_list.append(unit["Name"])
    namesLower = [nome.lower() for nome in names_list]
    NarakiFEU()