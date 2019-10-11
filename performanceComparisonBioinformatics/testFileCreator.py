import random

for i in range (5,13):
	with open("fasta_test"+str(i)+".fasta","w")as f:
		f.write(">test"+str(i)+"\n")
		s=""
		for i in range(0,pow(2,i)*4):
			r=random.randint(0,3)
			if(r==0):
				s+="A"
			elif(r==1):
				s+="T"
			elif(r==2):
				s+="G"
			else:
				s+="C"
			if(i%61==0):
				s+="\n"
		f.write(s)
	f.close()
