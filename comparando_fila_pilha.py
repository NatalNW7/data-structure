import random 

from datetime import datetime
from pilha.pilha import Pilha 
from filas.fila_circular import FilaCircular


def empilhar(lista):
    pilha = Pilha(len(lista), int)
    for i in lista:
        pilha.empilhar(i)
    return pilha

def enfileirar(lista):
    fila = FilaCircular(len(lista))
    for i in lista:
        fila.enfileirar(i)
    return fila

elementos = []
for _ in range(1000):
    elementos.append(round(random.randint(1, 100)))


startTime = datetime.now()
pilha = empilhar(elementos)
print('Pilha:', datetime.now() - startTime)

startTime = datetime.now()
fila = enfileirar(elementos)
print('Fila:', datetime.now() - startTime)