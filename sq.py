def buscar(matriz,nNodos,inicial,contador,camino):
	# print contador
	# print "\n".join(map(str,matriz))
	# raw_input(camino)

	for j in range(nNodos):
		if matriz[inicial][j]==1:
			matriz[inicial][j]=0
			if len(camino)>0 and camino[0]==j and (contador+1)==5:
				return 1
			elif (contador+1)<5:
				aux=buscar(matriz,nNodos,j,contador+1,camino+[j])
				if aux==1:
					return 1
			matriz[inicial][j]=1
	return -1
			

def crearMatriz(aristas,nNodos):
	matriz=[[0 for i in range(nNodos)] for j in range(nNodos)]
	for i in aristas:
		matriz[i[0]-1][i[1]-1]=1
	return matriz
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
	aristas.sort(key=lambda x:x[0])
	# raw_input(aristas)
	matriz=crearMatriz(aristas,nNodos)
	salida.append(-1)
	for i in range(nNodos):
		# print i
		if buscar(matriz,nNodos,i,1,[i])==1:
			salida[-1]=1
			break
print " ".join(map(str,salida))