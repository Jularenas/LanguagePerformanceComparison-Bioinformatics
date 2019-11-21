import subprocess
import os
import psutil
from threading import Thread
from time import sleep
import time
import timeit
import sys
cmd='cmd /C'
memories=[]

commands=sys.argv[1:]

strCommand=""

for c in commands:
	strCommand+=c+" "

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

print("measureStart")	
#CommandExecution
done=False
#threadMemoryTrack
thread = Thread(target = threaded_function)
thread.start()
thread2 = Thread(target = threaded_function)
thread2.start()
initMemory=psutil.virtual_memory()._asdict()

print("Your command: ",strCommand)
proc = subprocess.Popen([cmd+strCommand], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(stdout, stderr) = proc.communicate()
print("command executed")
done=True
thread.join()
usedVals=[]
for item in memories:
	usedVals.append(item['used'])
print(max(usedVals)-initMemory['used'])