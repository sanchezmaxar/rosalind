#heapsort
#leyendo el documento
#creando el maxHeap
def verificar(numeros):
	#va de atras para adelante barriendo los mayores hasta adelante
	cond=False
	i=len(numeros)-1
	while i>0:
		if (numeros[(i/2)-((i%2)^1)]<numeros[i]):
			numeros[(i/2)-((i%2)^1)],numeros[i]=numeros[i],numeros[(i/2)-((i%2)^1)]
			cond=True
		i-=1
	return cond

def maxHeap(numeros):
	while (verificar(numeros)): #mientras se mueva algo 
		pass
	return numeros

def postAcomodo(numeros): # acomoda los numeros en un maxheap, cuando se le quita el ultimo
	i=0
	while (i<len(numeros)):
		try:
			if (numeros[i*2+1]>numeros[i*2+2]):
				indice=i*2+1
			else:
				indice=i*2+2
		except:
			try:
				indice=i*2+1
				numeros[i],numeros[indice]=numeros[indice],numeros[i]
				return numeros
			except:
				return numeros
		if numeros[i]<numeros[indice]:
			numeros[i],numeros[indice]=numeros[indice],numeros[i]
		else:
			return numeros
		i=indice
	return numeros

def heapSort(numeros):
	salida=[]
	numeros=maxHeap(numeros)
	n=0
	while len(numeros)>1:
		numeros[0],numeros[-1]=numeros[-1],numeros[0]
		salida.append(numeros.pop())
		numeros=postAcomodo(numeros)
	salida.append(numeros.pop(0))
	return salida[::-1]

arch=open("prueba.txt","r")
nNum=int(arch.readline())
numeros=map(int,arch.readline().split(" "))
numeros.sort()
k=int(arch.readline())
# numeros=heapSort(numeros)
print " ".join(map(str,numeros[:k]))
# numeros.sort()

