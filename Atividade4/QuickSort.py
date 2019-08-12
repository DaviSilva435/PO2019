from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randrange
  
def geraListaI(tam):
    lista =[]
    while tam:
      lista.append(tam)
      tam-=1
    return lista  

def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def QuickSort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst
        
mpl.use('Agg')


def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista Invertida")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


x = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
yI = []
tempoI = []


for i in range(len(x)):
    yI.append(geraListaI(x[i]))

for i in range(len(x)):
    tempoI.append(timeit.timeit("QuickSort({})".format(yI[i]), setup="from __main__ import QuickSort", number=1))

desenhaGrafico(x, tempoI, "graphTempo.png")
