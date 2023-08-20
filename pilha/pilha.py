import numpy as np

class Pilha:
    def __init__(self, capacidade, dtype) -> None:
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=dtype)

    def __pilha_cheia(self):
        return True if self.__topo == self.__capacidade - 1 else False

    def __pilha_vazia(self):
        return True if self.__topo == -1 else False
    
    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('Pilha Cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha Vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1

if __name__ == '__main__':

    pilha = Pilha(5, int)
    print(pilha.ver_topo())            

    pilha.empilhar(1)
    print(pilha.ver_topo())            
    pilha.empilhar(2)
    pilha.empilhar(3)
    pilha.empilhar(4)
    pilha.empilhar(5)
    pilha.empilhar(6)
    print(pilha.ver_topo())            
    pilha.desempilhar()
    pilha.desempilhar()
    print(pilha.ver_topo())            
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.desempilhar()




















