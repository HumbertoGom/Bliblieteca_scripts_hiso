registros = [
    ["ABC1234", "entrada", 8],
    ["XYZ0001", "entrada", 9],
    ["ABC1234", "saída", 11],
    ["XYZ0001", "saída", 18],
    ["ABC1234", "entrada", 20]
]

entradas = {}
saidas = {}
horas={}
for registro in registros:
    placa= registro[0]
    acao= registro[1]
    hora= registro[2]
    if acao == 'entrada':
        entradas[placa]+=entradas.get(placa, 0) + 1
        horas[placa]-= hora
    if acao == 'saída':
        saidas[placa]+=saidas.get(placa, 0) + 1
        horas[placa]+= hora

print(entradas,saidas,horas)