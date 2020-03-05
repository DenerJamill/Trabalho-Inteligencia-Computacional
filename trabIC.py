def remedio(txt):
    if txt.lower() in 'febre, dor de cabeça':
        print(f'Você está com {txt.upper()}? Tome DIPIRONA')
    elif txt.lower() in 'gripe':
        print(f'Você está com {txt.upper()}? Tome BENEGRIPE')


def outro(txt):
    pass


def funcao(arquivo):
    arquivo = open(arquivo + '.txt', 'r+')
    texto = arquivo.read()
    medico = ['gripe', 'febre', 'dor de cabeça']
    for i in range(len(medico)):
        if medico[i] in texto.lower():
            print(f'Tem a palavra {medico[i].upper()}')
            remedio(medico[i])


funcao('teste')
