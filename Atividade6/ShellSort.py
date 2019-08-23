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
    ax.plot(x, y, label="Gráfico de Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)
    
def Shell_Sort(vetor):
    n = len(vetor)
    A = n // 2

    while A > 0:
        for i in range(A, n):
            op = vetor[i]
            k = i
            while k >= A and vetor[k - A] > op:
                vetor[k] = vetor[k - A]
                k -= A
            vetor[k] = op
        A //= 2

x = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
tempo = []

for i in range(len(x)):
    y.append(geraLista(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("Shell_Sort({})".format(y[i]), setup="from __main__ import Shell_Sort", number=1))

desenhaGrafico(x, tempo, "ShellTempo.png")
