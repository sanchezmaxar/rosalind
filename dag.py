def quita(aristas,numero):
	i=0
	while (i<len(aristas)):
		if aristas[i][0]==numero:
			aristas.pop(i)
		else:
			i+=1
def quitarInutiles(aristas,nNodos):
	i=0
	while (i<(nNodos-1)):
		if prueba(i+2,aristas)==False:
			quita(aristas,i+2)
		i+=1
def prueba(numero, aristas):
	salida=False
	for i in  aristas:
		if  i[1]==numero:
			return True
	return False	
def crearDic(aristas,nNodos):
	dic={}
	aux=aristas[0][0]
	auxi=0
	for i in range(len(aristas)):
		if aristas[i][0]>aux:
			dic[aux]=(auxi,i)
			aux=aristas[i][0]
			auxi=i
	dic[aux]=(auxi,i+1)
	return dic

def traer(aristas,numero,dic):
	try:
		inicio,final=dic[numero]
	except:
		return []
	i=inicio
	nodos=[]
	while i<final:
		nodos.append(aristas[i][1])
		i+=1
	return nodos
def suma(lista1,lista2):
	salida=lista2
	salida2=[]
	for i in lista1:
		if (i in lista2)==False:
			salida2.append(i)
	return [salida+salida2,salida2]


def ciclo(aristas,nNodos,dic):
	for i in range(nNodos):
		# print "para i = "+str(i+1)
		listaActual=traer(aristas,i+1,dic)
		listaAux=listaActual[:]
		listaAnterior=[]
		# raw_input(listaActual)
		while (listaAux!=[]):
			listaAux2=[]
			for j in listaAux:
				listaAux2+=traer(aristas,j,dic)
			listaAux=listaAux2
			listaActual,listaAux=suma(listaAux,listaActual)
			# raw_input(listaActual)
			if i+1 in listaActual:
				return -1
	return 1
import sys
arch=open(sys.argv[1],"r")
nGr=int(arch.readline())
salida=[]
aux=arch.readline()
for i in range(nGr):
	aristas=[]
	nNodos,nAristas=map(int,arch.readline().split(" "))
	aux=arch.readline()
	while aux!="\n" and aux!="":
		aristas.append(map(int,aux.split(" ")))
		aux=arch.readline()
	quitarInutiles(aristas,nNodos)
	aristas.sort(key=lambda x:x[0])
	dic=crearDic(aristas,nNodos)
	# print dic
	# raw_input(aristas)
	salida.append(ciclo(aristas,nNodos,dic))
print " ".join(map(str,salida))