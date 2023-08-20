class No():
    def __init__(self, valor) -> None:
        self.anterior = None
        self.valor = valor
        self.proximo = None
        
    def mostrar_no(self):
        print(self.valor)


if __name__ == '__main__':
    no = No(None)
    
    print(no.valor == None)