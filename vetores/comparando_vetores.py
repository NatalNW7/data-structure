import random 

from datetime import datetime
from vetor_nao_ordenado import VetorNaoOrdenado
from vetor_ordenado import VetorOrdenado


def insere_nao_ordenado(lista):
    vetor = VetorNaoOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def insere_ordenado(lista):
    vetor = VetorOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def pesquisa_nao_ordenado(lista):
    for i in lista:
        vetor_nao_ordenado.pesquisar(i)

def pesquisa_ordenado(lista):
    for i in lista:
        vetor_ordenado.pesquisa_binaria(i)

elementos = []
for _ in range(1000):
    elementos.append(round(random.randint(1, 100)))

pesquisa = []
for _ in range(1000):
    pesquisa.append(round(random.random(), 4))

print('Inserção')
startTime = datetime.now()
vetor_nao_ordenado = insere_nao_ordenado(elementos)
print('Vetor Não Ordenado:', datetime.now() - startTime)

startTime = datetime.now()
vetor_ordenado = insere_ordenado(elementos)
print('Vetor Ordenado:', datetime.now() - startTime)

# print('Pesquisa')
# startTime = datetime.now()
# pesquisa_nao_ordenado(pesquisa)
# print('Vetor Não Ordenado:', datetime.now() - startTime)

# startTime = datetime.now()
# pesquisa_ordenado(pesquisa)
# print('Vetor Ordenado:', datetime.now() - startTime)

vetor_ordenado.pesquisa_binaria(33)
