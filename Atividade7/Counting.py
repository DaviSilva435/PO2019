from random import randint
from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def geraLista(tam):
    vetor = list(range(1, tam + 1))
    shuffle(vetor)
    return vetor

def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Tamanho da lista de números x Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

def Counting(vetor):
    num_max = max(vetor)
    aux = [0] * (num_max + 1)
    for i in range(len(vetor)):
        aux[vetor[i]] += 1
    x = 0
    for i in range(len(aux)):
        a = aux[i]
        for _ in range(a):
            vetor[x] = i
            x += 1

x = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
tempo = []

for i in range(len(x)):
    y.append(geraLista(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("Counting({})".format(y[i]), setup="from __main__ import Counting", number=1))

desenhaGrafico(x, tempo, "Grafico.png")
