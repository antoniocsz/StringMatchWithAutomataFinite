# -*- coding: utf-8 -*-

def pega_valores():
    quantidade = int(input)
    texto = input()
    padrao = input()
    return quantidade, texto, padrao

def get_alfabeto(padrao):
    '''Retorna o alfabeto que está contido no padrão.'''
    alfabeto = []
    for i in padrao:
        if i not in alfabeto:
            alfabeto.append(i)
    return alfabeto


def verifica(T, trans, m):
    s = 0
    for i, c in enumerate(T):
        s = trans[s][c]
        if s == m:
            return i-m+1
    return -1


#import string as st
def transicao(padrao):
    alphabet = get_alfabeto(padrao)
    #alphabet = st.ascii_letters+st.punctuation+st.digits+st.whitespace
    m = len(padrao)
    trans = [ {c:0 for c in alphabet} for i in range(m) ]
    for s in range(m):
        for c in alphabet:
            k = min(m, s+1)
            while (padrao[:s]+c)[-k:] != padrao[:k]:
                k-=1
            trans[s][c]=k
    return trans

def main(valores):
    opcao = input()
    while opcao != 'e':
        if opcao == 's':
            ocorrencias = verifca(valores[1], transicao(valores[2]), len(valores[2]))
        if opcao == 'u'
        
        opcao = input()


# padrao = 'ababaca'
# texto = 'aabaababbabaaabacaababaababababbcabcbacbabcabcbabcaabababaca'
#
# print (string_matching_FSM(texto, transicao(padrao), len(padrao)))


if __name__ == '__main__':
    valores = pega_valores()
    main(valores)
