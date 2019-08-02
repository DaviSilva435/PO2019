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
  
mpl.use('Agg')

def SelectionSort(lista):
  for i in range(len(lista)): 
    indexadorMinimo=i 
    for j in range(i+1, len(lista)): 
        if lista[indexadorMinimo]>lista[j]: 
            indexadorMinimo=j 
    aux=lista[i]
    lista[i]=lista[indexadorMinimo]
    lista[indexadorMinimo]=aux
  return lista

print(SelectionSort(geraLista(30)))
  
def desenhaGrafico(x,y,y2,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo. Requisições x Tempo")
    ax.plot(x,y2, label = "Numero de Swaps. Requisições x Nº Operações")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')
   
x2 = [100,200,300,400]
y = []
y2= []
  
for i in range(4):
    y.append(timeit.timeit("SelectionSort({})".format(x2[i]),setup="from __main__ import SelectionSort",number=1))  
  
    y2.append(timeit.timeit("SelectionSort({})".format(x2[i]),setup="from __main__ import SelectionSort",number=1)) 
  
desenhaGrafico(x2,y,y2)
