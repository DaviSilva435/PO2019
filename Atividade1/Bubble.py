from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

x2 = [100,200,500,1000]
y = []
vetor2 = []

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saidas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')

def bubble(vetor):
    count = 0
    if len(vetor) <= 1:
        ordenado = vetor
    else:
        for j in range(0,len(vetor)):
            for i in range(0,len(vetor)-1):
                if vetor[i]>vetor[i+1]:
                    aux = vetor[i+1]
                    vetor[i+1] = vetor[i]
                    vetor[i] = aux
                    count+=1
        ordenado = vetor
    return ordenado

def geraLista(tam):
    vetor = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in vetor: vetor.append(n)
    return vetor
    
  
for i in x2:
  vetor2.append(geraLista(i))
  
for i in range(4):
    y.append(timeit.timeit("bubble({})".format(vetor2[i]),setup="from __main__ import bubble",number=1))  

desenhaGrafico(x2,y)
