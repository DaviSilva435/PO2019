
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

def desenhaGrafico(x,lista1,lista2,xl = "Entradas", yl = "Y",name="out",label1 ="Lista Randomica", label2 = "Lista Invertida"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.plot(x, lista2, label = label2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

graf_operacoes1 =[]
graf_operacoes2 =[]
def sort1(lista):
    count=0
    gap = int(len(lista)/2)
    
    while (gap > 0):
    
        for i in range(gap,len(lista)):
        
            aux = lista[i]
            j = i
            while(lista[j-gap] > aux and j >= gap  ):
                lista[j] = lista[j-gap]
                j = j-gap
                count+=1
            lista[j] = aux
            count+=1
            
        gap = int(gap/2)
    graf_operacoes1.append(count)    
def sort2(lista):
    count=0
    gap = int(len(lista)/2)
    
    while (gap > 0):
    
        for i in range(gap,len(lista)):
        
            aux = lista[i]
            j = i
            while(lista[j-gap] > aux and j >= gap  ):
                lista[j] = lista[j-gap]
                j = j-gap
                count+=1
            lista[j] = aux
            count+=1
            
        gap = int(gap/2)
        
    graf_operacoes2.append(count)    
    
    


quant = [100, 200, 500, 1000]
graf_tempo1 = []
graf_tempo2 = []
for i in range(len(quant)):
    print(quant[i])
    lista1 = geraLista(quant[i])
    lista2 = geraListaInvertida(quant[i])
    graf_tempo1.append(timeit.timeit("sort1({})".format(lista1),setup="from __main__ import sort1",number=1))
    graf_tempo2.append(timeit.timeit("sort2({})".format(lista2), setup="from __main__ import sort2", number=1))

desenhaGrafico(quant,graf_tempo1,graf_tempo2,"Tamanho", "Tempo", "saida_time")
desenhaGrafico(quant,graf_operacoes1,graf_operacoes2, "Tamanho", "Operacoes", "saida_operacoes")

