import numpy as np

class FilaCircular:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila Cheia')
            return
        
        if self.final == self.capacidade == -1:
            self.final = -1
        
        self.final +=1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila Vazia')
            return
        
        temp = self.valores[self.inicio]
        self.inicio += 1

        if self.inicio == self.capacidade:
            self.inicio = 0
        
        self.numero_elementos -= 1
        return temp
    
    def primeiro(self):
        return -1 if self.__fila_vazia() else self.valores[self.inicio]
        


if __name__ == '__main__':
    fila = FilaCircular(5)

    fila.enfileirar(1)
    print(fila.primeiro())
    fila.enfileirar(2)
    fila.enfileirar(3)
    fila.enfileirar(4)
    fila.enfileirar(5)
    fila.enfileirar(6)
    print(fila.primeiro())

    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    print(fila.primeiro())
    fila.enfileirar(6)
    fila.enfileirar(7)
