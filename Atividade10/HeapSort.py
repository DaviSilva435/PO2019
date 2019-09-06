from random import randint
from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')


def geraLista(tam):
    vetor = list(range(1, tam + 1))
    shuffle(vetor)
    return vetor


def Ordena(vetor, n, i):
    maior = i
    e = 2 * i + 1
    d = 2 * i + 2

    if e < n and vetor[i] < vetor[e]:
        maior = e

    if d < n and vetor[maior] < vetor[d]:
        maior = d

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]

        Ordena(vetor, n, maior)


def Heap_Sort(vetor):
    n = len(vetor)

    for i in range(n, -1, -1):
        Ordena(vetor, n, i)

    for i in range(n - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        Ordena(vetor, i, 0)


def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Tamanho da vetor de números x Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


x = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
tempo = []

for i in range(len(x)):
    y.append(geraLista(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("Heap_Sort({})".format(y[i]), setup="from __main__ import Heap_Sort", number=1))

desenhaGrafico(x, tempo, "Tempo.png")
