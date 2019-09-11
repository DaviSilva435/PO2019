from random import randint
from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')

x = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
tempo = []

def geraLista(tam):
    vetor = list(range(1, tam + 1))
    shuffle(vetor)
    return vetor

def Gnome(vetor):
    tam = len(vetor)
    x = 0
    while x < tam:
        if x == 0:
            x = x + 1
        if vetor[x] >= vetor[x - 1]:
            x = x + 1
        else:
            aux = vetor[x]
            vetor[x] = vetor[x - 1]
            vetor[x - 1] = aux
            x = x - 1
    return vetor


def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Tamanho da lista de números x Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

for i in range(len(x)):
    y.append(geraLista(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("Gnome({})".format(y[i]), setup="from __main__ import Gnome", number=1))

desenhaGrafico(x, tempo, "Tempo.png")
