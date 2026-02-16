Secreta = 'manteiga'
descoberta = '********'
tentativ = 0
while True:
    entrada = input('digite uma letra: ')
    for i in Secreta:
        if entrada == i:
            descoberta[i] = entrada
        else:
            print('*')
    print(descoberta)
    if descoberta == Secreta:
        print(' parabens voçê descobriu a palavra')
        print(f'levou apenas {tentativ} tentativas ')
    else:
        tentativ += 1
    