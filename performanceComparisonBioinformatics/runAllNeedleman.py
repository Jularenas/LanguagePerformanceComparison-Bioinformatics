import subprocess
import os
import psutil
from threading import Thread
from time import sleep
import timeit

langs=["javascript","java/needle","C","python","Go","rust"]
excmds=["node pairedAlignment.js","java -cp bin main.Needleman","needleman.exe","python pairedAlignment.py","go run needleman.go","needleman.exe"]
cmd='cmd /C'
memories=[]
#cpus=[]
done=False

def threaded_function():
	global memories
	global done		
	start = timeit.timeit()
	while not done:
		#cpus.append(psutil.cpu_percent())
		memories.append(psutil.virtual_memory()._asdict())
		end = timeit.timeit()
		if(end - start>5):
			time.sleep(5);
			start=time.timeit()
	print("done")



with open('op2.csv','w')as op:
	for lang in langs:		
		os.chdir(lang)
		op.write(lang+"\n")
		op.write("size;memory\n")
		for i in range(5,12):
			done=False
			#threadMemoryTrack
			thread = Thread(target = threaded_function)
			thread.start()
			thread2 = Thread(target = threaded_function)
			thread2.start()
			
			
			#input
			file1="fasta_test"+str(i)+".fasta"
			file2="fasta_test"+str(i)+"_2.fasta"
			
			#initial memory
			initMemory=psutil.virtual_memory()._asdict()
			#init cpu
			#initCpu=psutil.cpu_percent()
			
			#CommandExecution
			command=excmds[langs.index(lang)]+" "+file1+" "+file2
			proc = subprocess.Popen([cmd+str(command)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			(stdout, stderr) = proc.communicate()
			done=True
			thread.join()
			
			#op.write(str(pow(2,i)*2)+";"+str((max(cpus)-initCpu))+"\n")
			#cpus=[]
			usedVals=[]
			for item in memories:
				usedVals.append(item['used'])
			print(max(usedVals)-initMemory['used'])
			op.write(str(pow(2,i)*2)+";"+str((max(usedVals)-initMemory['used'])-(len(memories)*4))+"\n")
			#memories=[]
			#opStr=str(stdout.decode('utf-8'))
			#argsOp=opStr.split("\n")
			#timeSp=argsOp[len(argsOp)-2].split(":")[1].split(" ")
			#print(timeSp[1])
			#op.write(str(pow(2,i)*2)+";"+timeSp[1]+"\n")
			#print(str(stdout.decode('utf-8')))
			#print(str(stderr.decode('utf-8')))
		os.chdir("..")
		if(lang=="java/needle"):
			os.chdir("..")
		