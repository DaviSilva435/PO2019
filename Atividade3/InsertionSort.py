from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
  
def geraListaInversa(tam):
    lista = []
    for i in range(tam):
        lista.append(tam)
        tam = tam-1
    return lista

def InsertionSort(lista):
    contador_alteracoes = 0
    for i in range (1,len(lista)):
      valor = lista[i]
      j = i -1
      while j>=0 and valor<lista[j]:
        lista[j+1] = lista[j]
        j = j-1
        contador_alteracoes= contador_alteracoes+1
      lista[j+1] = valor
    return lista
  
mpl.use('Agg')
  
def desenhaGrafico(x,y,y2,nome_arquivo,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista Comum")
    ax.plot(x,y2, label = "Lista Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(nome_arquivo)

x = [1000,2000,5000,10000]
y = []
yInverso = []
tempo= []
tempoInverso = []
iteracoes = []
iteracoes2 = []
  
for i in range(len(x)):
    y.append(geraLista(x[i]))
    yInverso.append(geraListaInversa(x[i]))
    
  
for i in range(len(x)):
    tempo.append(timeit.timeit("InsertionSort({})".format(y[i]),setup="from __main__ import InsertionSort",number=1))  
    tempoInverso.append(timeit.timeit("InsertionSort({})".format(yInverso[i]),setup="from __main__ import InsertionSort",number=1))  
  
desenhaGrafico(x,tempo,tempoInverso, "grafoTempo.png")

for i in range(len(x)):
    iteracoes.append(InsertionSort(geraLista(x[i])))
    iteracoes2.append(InsertionSort(geraListaInversa(x[i])))
    
desenhaGrafico(x,iteracoes,iteracoes2, "grafoInteracoes.png")
