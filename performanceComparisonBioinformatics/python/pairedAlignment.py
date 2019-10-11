import math
import numpy
import time
import sys
cadena1=''
cadena2=''
gap=2
mut=1
score=float(0)
def dinamica(cadena1,cadena2):
	##
	##Construccion matriz dinamica
	##

	w = len(cadena2)+1;
	h=len(cadena1)+1;
	matrizDinamica = numpy.zeros([h,w])
	#print(str(w)+"-----"+str(h))
	##llenarScoresBase

	for i in range (0,len(matrizDinamica)):
		matrizDinamica[i][0]=i*gap
		#print(matrizDinamica[i][0])

	for i in range (0,len(matrizDinamica[0])):
		matrizDinamica[0][i]=i*gap
		#print(matrizDinamica[0][i])
		
	for i in range(1,len(matrizDinamica)):
		for j in range (1,len(matrizDinamica[i])):
			upVal=matrizDinamica[i-1][j]
			leftVal=matrizDinamica[i][j-1]
			diagVal=matrizDinamica[i-1][j-1]
			costUp=upVal+gap
			costLeft=leftVal+gap
			costDiag=diagVal
			if(cadena1[i-1]!=cadena2[j-1]):
				costDiag=costDiag+mut
			matrizDinamica[i][j]=min(min(costDiag,costUp),costLeft)

	score=matrizDinamica[len(matrizDinamica)-1][len(matrizDinamica[0])-1]			
	#print(len(cadena1))
	#print(len(cadena2))
	#print(matrizDinamica)
	print(score)
	#print(matrizDinamica.shape)
	#print(matrizDinamica[0][10])
	#print(matrizDinamica[10][0])
	#print(matrizDinamica)
	#print(len(cadena1))

files=sys.argv
file1=files[1]
file2=files[2]
with open("fastaFiles/"+file1,"r")as f:
	i=0
	for l in f:
		if(i!=0):
			cadena1+=l
		else:
			i+=1
with open("fastaFiles/"+file2,"r")as f2:
	i=0
	for l in f2:
		if(i!=0):
			cadena2+=l
		else:
			i+=1
			
d1=cadena1.split("\n")
d2=cadena2.split("\n")
cad1=""
cad2=""
for d in d1:
	cad1+=d
	
for d in d2:
	cad2+=d
dinamica(cad1,cad2)