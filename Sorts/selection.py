import timeit
from random import randint
import matplotlib.pyplot as plt

def geraListaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam-=1
    return lista

      
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,lista1,lista2,xl = "Entradas", yl = "Y",name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = "Lista Randomica")
    ax.plot(x, lista2, label = "Lista Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

graf_operacoes1 =[]
graf_operacoes2 =[]
def selection1(lista):
    count=0
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
            if lista[i] != lista[minimo]:
                lista[minimo], lista[i] = lista[i], lista[minimo]
                count+=1
    graf_operacoes1.append(count)


def selection2(lista):
    count=0
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
            if lista[i] != lista[minimo]:
                lista[minimo], lista[i] = lista[i], lista[minimo]
                count+=1
    graf_operacoes2.append(count)


quant = [10000, 20000, 50000, 100000]
graf_tempo1 = []
graf_tempo2 = []
for i in range(len(quant)):
    print(quant[i])
    lista1 = geraLista(quant[i])
    lista2 = geraListaInvertida(quant[i])
    graf_tempo1.append(timeit.timeit("selection1({})".format(lista1),setup="from __main__ import selection1",number=1))
    graf_tempo2.append(timeit.timeit("selection2({})".format(lista2), setup="from __main__ import selection2", number=1))

desenhaGrafico(quant,graf_tempo1,graf_tempo2,"Tamanho", "Tempo", "saida_time")
desenhaGrafico(quant,graf_operacoes1,graf_operacoes2, "Tamanho", "Operacoes", "saida_operacoes")
