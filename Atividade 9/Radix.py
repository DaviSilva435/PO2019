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


def Radix_Sort(vetor):
    aux = 1
    maximo = max(vetor)

    while maximo / aux > 0:
        x = len(vetor) + 1
        vetor2 = [0] * x

        for i in vetor:
            vetor2[i] += 1
        k = 0

        for i in range(x):
            for j in range(vetor2[i]):
                vetor[k] = i
                k += 1
        aux *= 10


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
    tempo.append(timeit.timeit("Radix_Sort({})".format(y[i]), setup="from __main__ import Radix_Sort", number=1))

desenhaGrafico(x, tempo, "Tempo.png")
