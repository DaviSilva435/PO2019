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
    gnome(lista)


def gnome(lista):
    index = 0
    while index < len(lista):
        if index == 0:
            index = index + 1
        if lista[index] >= lista[index - 1]:
            index = index + 1
        else:
            aux = lista[index]
            lista[index] = lista[index-1]
            lista[index-1] = aux
            index = index - 1
    

quant = [1000,2000,4000,5000,10000,20000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("sort({})".format(lista),setup="from __main__ import sort",number=1))


desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "saida_time", label1 = "Lista")
