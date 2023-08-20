from no import No

class ListaEncadeadaExtremidadeDupla:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None
         
    def __lista_vazia(self):
        return self.primeiro == None 
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.__lista_vazia():
            print('Lista Vazia')
            return

        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
        
    def insere_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.primeiro = novo
        else: 
            self.ultimo.proximo = novo

        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('Lista Vazia')
            return

        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
            
        self.primeiro = self.primeiro.proximo
        return temp

if __name__ == '__main__':
    lista = ListaEncadeadaExtremidadeDupla()

    lista.insere_inicio(1)
    print(lista.primeiro, lista.ultimo)

    lista.insere_inicio(2)
    lista.insere_inicio(3)
    lista.insere_inicio(4)
    lista.insere_inicio(5)
    lista.insere_inicio(6)

    lista.mostrar()
    print(lista.primeiro, lista.ultimo)
    print('-----')

    lista.insere_final(2)
    lista.insere_final(3)
    lista.insere_inicio(7)
    lista.insere_final(4)
    lista.mostrar()
    
    print('-----')
    lista.excluir_inicio()
    lista.excluir_inicio()
    lista.excluir_inicio()
    lista.mostrar()







