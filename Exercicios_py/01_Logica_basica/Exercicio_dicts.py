registros = [
    ["ABC1234", "entrada"],
    ["XYZ0001", "entrada"],
    ["ABC1234", "saída"],
    ["LMN4321", "entrada"],
    ["XYZ0001", "saída"],
]
corron = {}

for registro in registros:
    placa = registro[0]
    açao = registro[1]
    if açao =='entrada':
        corron[placa] = 1
    elif açao =='saída':
        corron[placa]= 0


for placa,estado in corron.items():
    if estado == 1:
        print(placa)
    
