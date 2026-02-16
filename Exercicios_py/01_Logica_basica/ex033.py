while True:
    frase = input('Digite uma frase')
    caminho= 'C:\\Users\\sarge\\OneDrive\\Documentos\\python-curso\\hisoka\\saida.txt'
    with open(caminho,'a') as arquivo:
        arquivo.write('\n' + frase)
    if frase == 'e':
        break