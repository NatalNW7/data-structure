from no import No

class ListaEncadeada:
    def __init__(self) -> None:
        self.primeiro = None
         
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def __lista_vazia(self):
        return self.primeiro == None

    def mostrar(self):
        if self.__lista_vazia():
            print('Lista Vazia')
            return
        
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('Lista Vazia')
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    
    def pesquisar(self, valor):
        if self.__lista_vazia():
            print('Lista Vazia')
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo

        return atual

    def excluir_posicao(self, valor):
        if self.__lista_vazia():
            print('Lista Vazia')
            return None

        atual = self.primeiro
        anterior = self.primeiro

        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual


if __name__ == '__main__':
    lista = ListaEncadeada()

    lista.insere_inicio(1)
    lista.mostrar()
    print('----')
    lista.insere_inicio(2)
    lista.mostrar()
    print('----')
    lista.insere_inicio(3)
    lista.insere_inicio(4)
    lista.insere_inicio(5)
    lista.mostrar()
    print('----')

    print(lista.excluir_inicio())
    lista.excluir_inicio()
    lista.excluir_inicio()
    lista.mostrar()
    print('----')

    lista.excluir_inicio()
    lista.mostrar()
    lista.excluir_inicio()
    lista.excluir_inicio()
    print('----')

    lista.insere_inicio(1)
    lista.insere_inicio(2)
    lista.insere_inicio(3)
    lista.insere_inicio(4)
    lista.insere_inicio(5)

    print(lista.pesquisar(5).valor)
    print(lista.pesquisar(3).valor)
    print(lista.pesquisar(10))
    
    print('----')
    print(lista.excluir_posicao(5).valor)
    print(lista.excluir_posicao(3).valor)
    print(lista.excluir_posicao(10))
    lista.mostrar()
    


