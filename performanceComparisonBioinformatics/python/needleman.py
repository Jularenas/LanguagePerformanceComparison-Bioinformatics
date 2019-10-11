import math
import numpy
import time
cadena1=''
cadena2=''
gap=2
mut=1
score=float(0)
#print(cadena1)
#print('----------------------')
#print('----------------------')
#print('----------------------')
#print('----------------------')
#print(cadena2)

def dinamica(cadena1,cadena2):
	##
	##Construccion matriz dinamica
	##
	w, h = len(cadena2)+1, len(cadena1)+1;
	matrizDinamica = numpy.zeros([h,w])
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
			if(matrizDinamica[i][j]==0):
				print(i,j)

	score=matrizDinamica[len(matrizDinamica)-1][len(matrizDinamica[0])-1]			
	#print(len(cadena1))
	#print(len(cadena2))
	#print(matrizDinamica)
	print(score)
	#print(matrizDinamica[0][10])
	#print(matrizDinamica[10][0])
	#print(matrizDinamica)
	#print(len(cadena1))
	
#for i in range(0,11):
#	cad1=''
#	cad2=''
#	for i in range(0,pow(2,i)):
#		cad1+='ATTCG'
#		cad2+='TATGC'
#	dinamica(cad1,cad2)	

with open("pythonResults.csv","w")as res:
	for i in range(5,13):
		dna1=''
		dna2=''
		with open("fastaFiles/fasta_test"+str(i)+".fasta",'r') as f1:
			l=0
			cs=0
			for line in f1:
				if(l!=0):
					line=line.rstrip()
					#cs=cs+len(line)
					#print(cs)
					dna1=dna1+line
				l=l+1
		cadena1=dna1
		f1.close()
		for j in range(5,13):
			with open("fastaFiles/fasta_test"+str(i)+"_2.fasta",'r') as f2:
				l=0
				for line in f2:
					if(l!=0):
						line=line.rstrip()
						dna2=dna2+line
					l=l+1
			cadena2=dna2
			tiempoinic=time.time()
			dinamica(cadena1,cadena2)
			tiempofin=time.time()
			timeD=str(tiempofin-tiempoinic)
			trs=timeD.split(".")
			timeString=""
			index=0
			for el in trs:
				if index==0:
					timeString+=el+"."
				else:
					timeString+=el
			index=index+1
			timeString=timeString[0:len(timeString)-2]
			res.write(str(len(cadena1))+";"+str(len(cadena2))+";"+timeString+"\n")
		f2.close()
res.close()