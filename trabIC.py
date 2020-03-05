def remedio(txt):
    """
    Essa função recebe uma doença da lista 'medico' e retorna um texto com a doença
    e o remédio a ser tomado.
    :param txt: Palavra(s) presente(s) na lista 'medico' encontrado(s) na leitura do arquivo txt.
    :return: Texto com a doença e o remédio a ser tomado.
    """
    rem = ''
    if txt.lower() in 'febre, dor de cabeça':
        rem = 'DIPIRONA'
    elif txt.lower() in 'gripe':
        rem = 'BENEGRIPE'
    return f'Você está com {txt.upper()}? Tome {rem.upper()}!'


def problema(txt):
    """
    Essa função recebe um problema da lista 'computador' e retorna um texto com
    o problema e uma provável solução.
    :param txt: Palavra(s) presente(s) na lista 'computador' encontrada(s) na leitura do arquivo txt.
    :return: Texto com o problema apresentado no pc e a indicação da provável peça defeituosa.
    """
    peca = ''
    if txt.lower() in 'não liga':
        peca = 'fonte ou alimentação'
    elif txt.lower() in 'tela azul':
        peca = 'memória ou registro'
    elif txt.lower() in 'relógio errado':
        peca = 'bateria'
    return f'O seu PC está com problema de {txt.upper()}? Então o problema deve estar na(o) {peca.upper()} do seu pc!'


def funcao(arquivo):
    """
    Essa função recebe um arquivo txt, e a partir da leitura, indica qual a função a ser usada.
    :param arquivo: Arquivo txt com o texto a ser lido.
    :return: A requisição e sua solução.
    """
    arquivo = open(arquivo + '.txt', 'r')
    texto = arquivo.read()
    medico = ['gripe', 'febre', 'dor de cabeça']
    computador = ['não liga', 'tela azul', 'relógio errado']
    for i in range(len(medico)):
        if medico[i] in texto.lower():
            print(f'Tem a palavra {medico[i].upper()}')
            print(remedio(medico[i]))
        if computador[i] in texto.lower():
            print(f'Tem a plavra {computador[i].upper()}!')
            print(problema(computador[i]))
    arquivo.close()


funcao('teste')
