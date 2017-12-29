import sys
sys.setrecursionlimit(10000)
def toInt(cadena):
	return map(int,cadena.split(" "))
def prueba(numero, aristas):
	salida=False
	for i in  aristas:
		if  i[1]==numero:
			return True
	return False	
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
def main(aristas):
	##primera vez
	siguientesVieja=funcion(1,0,aristas)
	siguientesNueva=[]
	cond=True
	nivel=1
	while (siguientesNueva!=[] or cond):
		if cond:
			cond=False
		siguientesNueva=[]
		for i in siguientesVieja:
			# print i
			siguientesNueva+=funcion(i,nivel,aristas)
		siguientesVieja=siguientesNueva
		nivel+=1
		# raw_input(salida)


def funcion(numero,nivel,aristas):
	cond=False # es para llegar al numero, ya que estan ordenados
	cond2=True # es para salir del ciclo una vez que ya se hayan terminado
	i=0
	siguientesVieja=[]
	siguientesNueva=[]
	global salida
	while (i<len(aristas)):
 		if aristas[i][0]==numero:
			if salida[aristas[i][1]-1]==-1:
				salida[aristas[i][1]-1]=nivel+1
			if (aristas[i][1] in siguientesNueva)==False:
				siguientesNueva.append(aristas[i][1])
			aristas.pop(i)
			i-=1
			if cond==False:
				cond=True
		elif cond:
			break
		i+=1
	return siguientesNueva
#se lee el archivo
arch=open("entradaLarga.txt","r")
nAristas,vertices=map(int,arch.readline().split(" "))
aristas=map(toInt,arch.readlines())
aristas.sort(key=lambda x:x[0])
arch.close()
#se inicializa la salida
salida=[-1 for i in range(nAristas)]
salida[0]=0
#quitamos  aristas inutiles
l1=len(aristas)
quitarInutiles(aristas,nAristas)
print l1-len(aristas)
try:
	main(aristas)
	print " ".join(map(str,salida))
except:
	print salida.count(-1)
	print salida
