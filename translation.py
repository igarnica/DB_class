import argparse
import math 

#Para crear un nodo
class Node: 
	def __init__(self): 
		self.A=None
		self.U=None
		self.C=None
		self.G=None

#El árbol tiene 4 niveles, y puesto que la manera de llegar al nodo del 4° nivel es única (cada camino es correspondiente a un codon), podemos
#utilizar el último nodo para guardar el aminoácido correspondiente al codon. 
class Node_fin: 
	def __init__(self,letter): 
		self.aa=letter

#Función para buscar la correspondencia de un codon con cierto aminoácido (el código genético está guardado en el árbol). Se pide la dirección
#del nodo, la posición de la secuencia con la que se va a comparar la letra y el número de iteraciones (al llegar a la cuarta iteración, 
#sabemos que estamos en el cuarto nivel donde está guardado la correspondencia del aminoácido y no es necesario continuar buscando en el árbol)
def busqueda(nodo,pos,iteracion):
	if(iteracion==4):
		return(nodo.aa)
	if(seq[pos]=="A"):
		return(busqueda(nodo.A,pos+1,iteracion+1))
	elif(seq[pos]=="U"):
		return(busqueda(nodo.U,pos+1,iteracion+1))
	elif(seq[pos]=="C"):
		return(busqueda(nodo.C,pos+1,iteracion+1))
	elif(seq[pos]=="G"):
		return(busqueda(nodo.G,pos+1,iteracion+1))

#Código para obtener datos de la terminal, usando los identificadores "-adn" o "-arn"
parser=argparse.ArgumentParser()
parser.add_argument("-adn",type=str,dest="adn")
parser.add_argument("-arn",type=str,dest="arn")
args=parser.parse_args()



#Para inicializar el árbol. El primer nodo nos manda a 4 nodos que corresponden al primer codon, cada uno de los nodos en el segundo nivel
#nos manda a nodos que corresponden al segundo codon, cada uno de los nodos en el tercer nivel nos mandan a nodos que corresponden al
#tercer codon. Si seguimos la secuencia de nodos de la raíz (primer nivel) a la tercer letra del codon (cuarto nivel), en el nodo del cuarto
#nivel hallaremos el aminoácido al que corresponde ese codon.
root=Node()

root.A=Node()

root.A.A=Node()
root.A.A.A=Node_fin("Lys")
root.A.A.U=Node_fin("Asn")
root.A.A.C=Node_fin("Asn")
root.A.A.G=Node_fin("Lys")

root.A.U=Node()
root.A.U.A=Node_fin("Ile")
root.A.U.U=Node_fin("Ile")
root.A.U.C=Node_fin("Ile")
root.A.U.G=Node_fin("Met")

root.A.C=Node()
root.A.C.A=Node_fin("Thr")
root.A.C.U=Node_fin("Thr")
root.A.C.C=Node_fin("Thr")
root.A.C.G=Node_fin("Thr")

root.A.G=Node()	
root.A.G.A=Node_fin("Arg")
root.A.G.U=Node_fin("Ser")
root.A.G.C=Node_fin("Ser")
root.A.G.G=Node_fin("Arg")	


root.U=Node()

root.U.A=Node()
root.U.A.A=Node_fin(" ")
root.U.A.U=Node_fin("Tyr")
root.U.A.C=Node_fin("Tyr")
root.U.A.G=Node_fin(" ")

root.U.U=Node()
root.U.U.A=Node_fin("Leu")
root.U.U.U=Node_fin("Phe")
root.U.U.C=Node_fin("Phe")
root.U.U.G=Node_fin("Leu")

root.U.C=Node()
root.U.C.A=Node_fin("Ser")
root.U.C.U=Node_fin("Ser")
root.U.C.C=Node_fin("Ser")
root.U.C.G=Node_fin("Ser")

root.U.G=Node()	
root.U.G.A=Node_fin(" ")
root.U.G.U=Node_fin("Cys")
root.U.G.C=Node_fin("Cys")
root.U.G.G=Node_fin("Trp")

root.C=Node()

root.C.A=Node()
root.C.A.A=Node_fin("Gln")
root.C.A.U=Node_fin("His")
root.C.A.C=Node_fin("His")
root.C.A.G=Node_fin("Gln")

root.C.U=Node()
root.C.U.A=Node_fin("Leu")
root.C.U.U=Node_fin("Leu")
root.C.U.C=Node_fin("Leu")
root.C.U.G=Node_fin("Leu")

root.C.C=Node()
root.C.C.A=Node_fin("Pro")
root.C.C.U=Node_fin("Pro")
root.C.C.C=Node_fin("Pro")
root.C.C.G=Node_fin("Pro")

root.C.G=Node()	
root.C.G.A=Node_fin("Arg")
root.C.G.U=Node_fin("Arg")
root.C.G.C=Node_fin("Arg")
root.C.G.G=Node_fin("Arg")	


root.G=Node()

root.G.A=Node()
root.G.A.A=Node_fin("Glu")
root.G.A.U=Node_fin("Asp")
root.G.A.C=Node_fin("Asp")
root.G.A.G=Node_fin("Glu")

root.G.U=Node()
root.G.U.A=Node_fin("Val")
root.G.U.U=Node_fin("Val")
root.G.U.C=Node_fin("Val")
root.G.U.G=Node_fin("Val")

root.G.C=Node()
root.G.C.A=Node_fin("Ala")
root.G.C.U=Node_fin("Ala")
root.G.C.C=Node_fin("Ala")
root.G.C.G=Node_fin("Ala")

root.G.G=Node()	
root.G.G.A=Node_fin("Gly")
root.G.G.U=Node_fin("Gly")
root.G.G.C=Node_fin("Gly")
root.G.G.G=Node_fin("Gly")
			

#Para guardar la secuencia que se va a traducir
	#Con ARN
if (args.adn==None):
	if(args.arn==None):
		print("Ingrese una secuencia usando -rna xor -dna")
		exit()
	else:
		seq=[""]*len(args.arn)
		args.arn=(args.arn).upper()
		seq=args.arn	
	#Con ADN (si existe tanto ADN como ARN, nos quedamos con el ARN)
else:
	seq=[""]*len(args.adn)
	args.adn=(args.adn).upper()
	args.adn=(args.adn).replace("T","U")
	seq=args.adn

aa=[""]*math.floor(len(seq)/3)
#Para realizar la búsqueda en el árbol que se creó arriba
for pos_global in range(0,math.floor(len(seq)/3)):
	aa[pos_global]=busqueda(root,3*pos_global,1)
	if(aa[pos_global]==" "):
		break

#Para convertir la lista de strings a un strings
aa=''.join(aa)
print(aa)
