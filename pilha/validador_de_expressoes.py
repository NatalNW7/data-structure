from pilha import Pilha


def validador_de_expressao(expressao):
    pilha = Pilha(10, str)
    empilha = '{(['
    desempilha = '])}'

    for caractere in expressao:
        if caractere in empilha:
            pilha.empilhar(caractere)

        if caractere in desempilha:
            if caractere == ']' and pilha.ver_topo() == '[':
                pilha.desempilhar()
            elif caractere == ')' and pilha.ver_topo() == '(':
                pilha.desempilhar()
            elif caractere == '}' and pilha.ver_topo() == '{':
                pilha.desempilhar()
            else:
                print('Expressão Irregular:', expressao)
                return
    
    print('Expressão Regular:', expressao)

validador_de_expressao('()')
validador_de_expressao('c[d]')
validador_de_expressao('a{c[d]}')
validador_de_expressao('a{b[c]d}e')
validador_de_expressao('a{b(c]d}e')
validador_de_expressao('a{b(c)d)e')
validador_de_expressao('a{b[cd}e')