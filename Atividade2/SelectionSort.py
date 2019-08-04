from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
	
  g1,g2 =[], []
  
	def geravetor1(tam):
	    vetor = []
	    while tam:
	        vetor.append(tam)
	        tam-=1
	    return vetor
    
  def OrdenaSS1(vetor):
	    count=0
	    for i in range(len(vetor)):
	        k = i
	        for j in range(i+1, len(vetor)):
	            if vetor[k] > vetor[j]:
	                k = j
	            if vetor[i] != vetor[k]:
	                vetor[k], vetor[i] = vetor[i], vetor[k]
	                count+=1
	    g1.append(count)
	
	def geravetor2(tam):
	    vetor = []
	    for i in range(tam):
	        numero = randint(1,1*tam)
	        if numero not in vetor: vetor.append(numero)
	    return vetor
    
	def OrdenaSS2(vetor):
	    count=0
	    for i in range(len(vetor)):
	        k = i
	        for j in range(i+1, len(vetor)):
	            if vetor[k] > vetor[j]:
	                k = j
	            if vetor[i] != vetor[k]:
	                vetor[k], vetor[i] = vetor[i], vetor[k]
	                count+=1
	    g2.append(count)
	
	def desenhaGrafico(x,vetor1,vetor2,xl = "Entradas", yl = "Y"):
	    fig = plt.figure(figsize=(10, 8))
	    ax = fig.add_subplot(111)
	    ax.plot(x, vetor1, label = "Aleatória")
	    ax.plot(x, vetor2, label = "Invertida")
	    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	    plt.ylabel(yl)
	    plt.xlabel(xl)
	    plt.savefig('PlotagemTempo.png')
	
	quant = [10000, 20000, 50000, 100000]
	modeloG1 = []
	modeloG2 = []
	for i in range(len(quant)):
	    print(quant[i])
	    vetor1 = geraVetor(quant[i])
	    vetor2 = geraVetorInvertida(quant[i])
	    modeloG1.append(timeit.timeit("OrdenaSS1({})".format(vetor1),setup="from __main__ import OrdenaSS1",number=1))
	    modeloG2.append(timeit.timeit("OrdenaSS2({})".format(vetor2), setup="from __main__ import OrdenaSS2", number=1))
	
	desenhaGrafico(quant,modeloG1,modeloG2,"Tamanho", "Tempo", "saida_time")
	desenhaGrafico(quant,g1,g2, "Tamanho", "Operacoes", "saida_operacoes")
