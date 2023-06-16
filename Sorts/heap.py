import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
      

def desenhaGrafico(x,lista1,xl = "Entradas", yl = "Y",name="out", label1 = "Lista 1", label2 = "Lista 2"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

def sort(lista):
    heap(lista)


def heap(lista):
    for i in range(len(lista), -1, -1):
        dist(lista, len(lista), i)

    for i in range(len(lista)-1, 0, -1):
        aux = lista[i]
        lista[i] = lista[0]
        lista[0] = aux
        dist(lista, i, 0)


def dist(lista, size, current):

    maxim = current
    left = 2 * current + 1
    right = 2 * current + 2

    if left < size and lista[current] < lista[left]:
        maxim = left
    if right < size and lista[maxim] < lista[right]:
        maxim = right
    if maxim != current:
        aux = lista[current]
        lista[current] = lista[maxim]
        lista[maxim] = aux
        dist(lista, size,maxim)



quant = [100000,200000,400000,500000,1000000,2000000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("sort({})".format(lista),setup="from __main__ import sort",number=1))


desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "saida_time", label1 = "Lista")
