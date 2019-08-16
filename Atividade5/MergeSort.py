from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraListaI(tam):
    lista =[]
    while tam:
      lista.append(tam)
      tam-=1
    return lista  

def MergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)

        vetorEsquerdo = lista[:meio]
        vetorDireito = lista[meio:]

        MergeSort(vetorEsquerdo)
        MergeSort(vetorDireito)

        i = 0
        j = 0
        k = 0

        while i < len(vetorEsquerdo) and j < len(vetorDireito):

            if vetorEsquerdo[i] < vetorDireito[j]:
                lista[k]=vetorEsquerdo[i]
                i += 1
            else:
                lista[k]=vetorDireito[j]
                j += 1
            k += 1

        while i < len(vetorEsquerdo):

            lista[k]=vetorEsquerdo[i]
            i += 1
            k += 1

        while j < len(vetorDireito):
            lista[k]=vetorDireito[j]
            j += 1
            k += 1
            
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
    tempoI.append(timeit.timeit("MergeSort({})".format(yI[i]), setup="from __main__ import MergeSort", number=1))

desenhaGrafico(x, tempoI, "graphTempo.png")
