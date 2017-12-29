#algoritmo de di
#primero es un bfs
import sys

def buscarNuevos(aristas,viejos,nivel,distancia):
	# print "Busca"
	nuevos=[]
	i=0
	posibles=[]
	nuevos=viejos[:]
	try:
		while viejos and i<len(aristas):
			# print viejos
			# print aristas
			# raw_input("posibles "+str(posibles))
			if aristas[i][0] in viejos:
				if aristas[i][0]> viejos[0]:
					# print "Aqui quita2"
					viejos.pop(0)
				posibles.append(aristas[i][2])
			elif aristas[i][0]>viejos[0]:
				# print "Aqui quita"
				viejos.pop(0)
			i+=1
	except:
		pass
	# print "nivel="+str(nivel)+"+"+str(min(posibles))
	if posibles==[]:
		return [[],42]
	nivel+=min(posibles)
	nuevos=restar(aristas,nuevos,min(posibles),nivel,distancia)
	nuevos.sort()
	return [nuevos,nivel]
def restar(aristas,viejos,salto,nivel,distancia):
	# print "Resta"
	nuevos=[]
	i=0
	while viejos and i<len(aristas):
		# print viejos
		# raw_input(aristas)
		if aristas[i][0] in viejos:
			if aristas[i][0]>viejos[0]:
				viejos.pop(0)
			aristas[i][2]-=salto
			if aristas[i][2]==0:
				if distancia[aristas[i][1]-1]==-1:
					# print "Aqui pone"
					distancia[aristas[i][1]-1]=nivel
				if (aristas[i][1] in nuevos)==False:
					nuevos.append(aristas[i][1])
				aristas.pop(i)
				i-=1
			else:
				if (aristas[i][0] in nuevos)==False:
					nuevos.append(aristas[i][0])
		elif aristas[i][0]>viejos[0]:
			viejos.pop(0)
		i+=1
	return nuevos


def bfs(aristas,nNodos):#saca la distancia del nodo 1 a todos
	nuevos=[1]
	distancia=[-1 for i in range(nNodos)]
	distancia[0]=0
	nivel=0
	while nuevos!=[]:
		# raw_input(distancia)
		nuevos,nivel=buscarNuevos(aristas,nuevos,nivel,distancia)
	return distancia


#abrimos el archivo
arch=open(sys.argv[1],"r")
nNodos,nAristas=map(int,arch.readline().split(" "))
aristas=[map(int,i.split(" ")) for i in arch.readlines()]
arch.close()
aristas.sort(key=lambda x:x[0])
# print aristas

print " ".join(map(str,bfs(aristas,nNodos)))

