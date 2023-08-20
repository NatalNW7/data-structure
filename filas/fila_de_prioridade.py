import numpy as np 

class FilaPrioridade:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def primeiro(self):
        return -1 if self.__fila_vazia() else self.valores[self.numero_elementos - 1]
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila Cheia')
            return
        
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos -1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -=1

            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila Vazia')
            return
        
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor


if __name__ == '__main__':
    fila = FilaPrioridade(5)

    print(fila.primeiro())

    fila.enfileirar(13)
    print(fila.primeiro())
    fila.enfileirar(13)
    fila.enfileirar(4)
    fila.enfileirar(15)
    fila.enfileirar(50)
    fila.enfileirar(55)
    print(fila.primeiro())
    print('-----')
    fila.desenfileirar()
    print(fila.primeiro())
    fila.desenfileirar()
    print(fila.primeiro())
    fila.desenfileirar()
    print(fila.primeiro())
    fila.desenfileirar()
    print(fila.primeiro())



