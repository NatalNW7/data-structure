import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print (i, '-', self.valores[i])

    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Não tem espaço')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        
        return -1
    
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -=1


if __name__ == '__main__':
    vetor = VetorNaoOrdenado(5)
    vetor.insere(2)
    vetor.insere(5)
    vetor.insere(10)
    vetor.insere(0)
    vetor.insere(7)
    vetor.imprime()
    vetor.insere(9)
        
    print(vetor.pesquisar(2))

    vetor.excluir(10)
    vetor.imprime()
    print('-----')
    vetor.excluir(2)
    vetor.imprime()
    print('-----')
    vetor.excluir(7)
    vetor.imprime()
    print('-----')

    vetor.insere(8)
    vetor.insere(9)
    vetor.insere(34)
    vetor.imprime()