from string import ascii_lowercase


def get_alfabeto():
    return ascii_lowercase + '., '


def trata_texto(texto):
    texto = texto.rstrip()
    return texto


def buscar_padrao(texto, transicoes):
    '''busca o padrao no texto'''
    tamanho = len(transicoes)
    estado = 0
    ocorrencias = []
    for count, char in enumerate(texto):
        estado = transicoes[estado][char]
        if estado == tamanho:
            ocorrencias.append(count - tamanho + 2)
            estado = 0
    return ocorrencias


def gerar_tabela(padrao):
    alfabeto = get_alfabeto()
    TAM = len(padrao)
    transicoes = [ {caracter : 0 for caracter in alfabeto} for i in range(TAM) ]
    for count in range(TAM):
        for caracter in alfabeto:
            k = min(TAM, count+1)
            while (padrao[:count]+caracter)[-k:] != padrao[:k]:
                k-=1
            transicoes[count][caracter]= 0 if k < 0 else k
    return transicoes


def gerar_tabela2(padrao):
    alfabeto = get_alfabeto()
    TAM = len(padrao)+1
    transicoes = [ {caracter : 0 for caracter in alfabeto} for i in range(TAM+1) ]
    for count in range(TAM):
        for caracter in alfabeto:
            k = min(TAM, count+1)
            while (padrao[:count]+caracter)[-k:] != padrao[:k]:
                k-=1
            transicoes[count][caracter]= 0 if k < 0 else k
    return transicoes


def imprimir_tabela(padrao):
    print ('Tabela Delta:')
    for index, lista in enumerate(padrao):
        for alf in get_alfabeto():
            for char, valor in lista.items():
                if alf == char:
                    print ('[{}, {}]: {} '.format(index, char, valor))
                    if alf == ' ':
                        print ("[{}, ’{}’]: {} ".format(index, char, valor))


def main(texto, padrao):
    opcao = input()
    while opcao != 'e':
        if opcao == 's':
            ocorrencias = buscar_padrao(texto, gerar_tabela(padrao))
            for ocorrencia in ocorrencias:
                print (ocorrencia)
        if opcao == 'u':
            tabela = gerar_tabela2(padrao)
            imprimir_tabela(tabela)
        opcao = input()
    exit()


if __name__ == '__main__':
    quantidade = int(input())
    texto = input()
    padrao = input()
    padrao = trata_texto(padrao)
    main(texto, padrao)
