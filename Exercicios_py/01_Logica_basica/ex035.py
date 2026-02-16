caminho= 'C:\\Users\\sarge\\OneDrive\\Documentos\\python-curso\\hisoka\\mensagem.txt'
with open(caminho,'r',encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    palavre = conteudo.split()
    palavras = len(palavre)
    print(palavras)