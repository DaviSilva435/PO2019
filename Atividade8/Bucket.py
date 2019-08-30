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


def bucketSort(vetor):
    def quickSort(vetor, st, fim):
        if st < fim:
            aux = randint(st, fim)
            x = vetor[fim]
            vetor[fim] = vetor[aux]
            vetor[aux] = x

            p = dividir(vetor, st, fim)
            quickSort(vetor, st, p - 1)
            quickSort(vetor, p + 1, fim)

        return vetor

    def dividir(vetor, st, fim):
        aux = randint(st, fim)
        vetor[fim], vetor[aux] = vetor[aux], vetor[fim]
        aux2 = st - 1
        for index in range(st, fim):
            if vetor[index] < vetor[fim]:
                aux2 = aux2 + 1
                vetor[aux2], vetor[index] = vetor[index], vetor[aux2]

        x = vetor[aux2 + 1]
        vetor[aux2 + 1] = vetor[fim]
        vetor[fim] = x

        return aux2 + 1

    maior = max(vetor)
    tam = len(vetor)
    size = maior / tam
    bucket = [[] for _ in range(tam)]

    for i in range(tam):
        j = int(vetor[i] / size)
        if j != tam:
            bucket[j].appfim(vetor[i])
        else:
            bucket[tam - 1].appfim(vetor[i])

    for i in range(tam):
        quickSort(bucket[i], 0, len(bucket[i]) - 1)

    result = []

    for i in range(tam):
        result = result + bucket[i]

    return result


def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Tamanho da vetor de números x Tempo")
    ax.legfim(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

x = [100000, 20000, 40000, 50000, 100000, 200000]
y = []
tempo = []

for i in range(len(x)):
    y.appfim(geraLista(x[i]))

for i in range(len(x)):
    tempo.appfim(timeit.timeit("bucketSort({})".format(y[i]), setup="from __main__ import bucketSort", number=1))

desenhaGrafico(x, tempo, "Tempo.png")
