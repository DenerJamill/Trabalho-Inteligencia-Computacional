def funcao(arquivo):
    arquivo = open(arquivo + '.txt', 'r+')
    texto = arquivo.read()
    medico = ['GRIPE', 'FEBRE']
    for i in range(len(medico)):
        if medico[i] in texto.upper():
            print(f'Tem a palavra {medico[i]}')


funcao('teste')
