# -*- coding: utf-8 -*-

def pega_valores():
    # quantidade = int(input())
    # texto = input()
    # padrao = input()
    # return (quantidade, texto, padrao)
    return None

def get_alfabeto(padrao):
    '''Retorna o alfabeto que está contido no padrão.'''
    alfabeto = []
    for i in padrao:
        if i not in alfabeto:
            alfabeto.append(i)
    return alfabeto


def buscar_padrao(texto, transicoes, tananho):
    estado = 0
    ocorrencias = []
    for count, char in enumerate(texto):
        estado = transicoes[estado][char]
        if estado == tananho:
            ocorrencias.append(count - tananho +1)
            estado = 0
    return ocorrencias


#import string as st
def gerar_tabela(padrao):
    alfabeto = get_alfabeto(padrao)
    #alfabeto = st.ascii_letters+st.punctuation+st.digits+st.whitespace
    TAM = len(padrao)
    transicoes = [ {caracter : 0 for caracter in alfabeto} for i in range(TAM) ]
    for count in range(TAM):
        for caracter in alfabeto:
            k = min(TAM, count+1)
            while (padrao[:count]+caracter)[-k:] != padrao[:k]:
                k-=1
            transicoes[count][caracter]=k
    return transicoes


def main(valores):
    opcao = input()
    while opcao != 'e':
        if opcao == 's':
            print (buscar_padrao('aabaababbababacaababaababababbcabcbacbabcabcbabcaabababaca', gerar_tabela('ababaca'), len('ababaca')))
        if opcao == 'u':
            pass
        opcao = input()
    exit()

# padrao = 'ababaca'
# texto = 'aabaababbabaaabacaababaababababbcabcbacbabcabcbabcaabababaca'
#
# print (string_matching_FSM(texto, gerar_tabela(padrao), len(padrao)))


if __name__ == '__main__':
    valores = pega_valores()
    main(valores)
