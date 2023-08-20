from no import No

class ListaDuplamenteEncadeada:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar_inicio(self):
        if self.__lista_vazia():
            print('Lista Vazia')
            return

        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
    
    def mostrar_final(self):
        if self.__lista_vazia():
            print('Lista Vazia')
            return

        atual = self.ultimo
        while atual != None:
            atual.mostrar_no()
            atual = atual.anterior
    
    def insere_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        
        self.ultimo = novo
    
    def excluir_inicio(self):
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            temp = self.primeiro
            temp.proximo.anterior = None
            self.primeiro = temp.proximo
            temp.proximo = None

            return temp
    
    def excluir_final(self):
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            temp = self.ultimo
            temp.anterior.proximo = None
            self.ultimo = temp.anterior

            return temp

    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                return None
        
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        
        return atual

  
if __name__ == '__main__':
    lista = ListaDuplamenteEncadeada()

    lista.insere_inicio(1)
    lista.insere_inicio(2)
    lista.insere_inicio(3)
    lista.insere_inicio(4)
    lista.insere_inicio(5)
    lista.mostrar_inicio()
    print('----')
    lista.mostrar_final()

    print('----')
    lista.insere_final(7)
    lista.insere_final(8)
    lista.mostrar_inicio()
    print('----')
    lista.mostrar_final()

    print('D----')
    lista.excluir_inicio()
    lista.mostrar_inicio()
    print('----')
    lista.excluir_final()
    lista.mostrar_inicio()
    print('----')
    lista.mostrar_final()
    
    print('----')
    lista.excluir_posicao(2)
    lista.mostrar_inicio()
    print('----')
    lista.mostrar_final()
    print('----')
    lista.excluir_posicao(1)
    lista.excluir_posicao(7)
    lista.mostrar_inicio()
    print('----')
    lista.mostrar_final()




