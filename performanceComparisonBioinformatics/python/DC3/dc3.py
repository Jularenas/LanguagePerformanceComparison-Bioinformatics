import radix

#cadena

cad='YABBADABBADO'

#construcción de alfabeto

alf=[]

for c in cad:
    alf.append(ord(c))
print(alf)

radix.radixSort(alf)

print(alf)

index=0
lastChar=-1
alfDict={}
for a in alf:
    if(a != lastChar):
        index+=1
        alfDict[chr(a)]=index
    lastChar=a
print(alfDict)
        
alfCad=[]
for c in cad:
    alfCad.append(alfDict[c])
print(alfCad)


#Crear sample set / b0

b1=[]
b2=[]
b0=[]
idx=0
b12idx=[]
for cd in alfCad:
    if(idx%3==1):
        b1.append((cd,idx))
    elif(idx%3==2):
        b2.append((cd,idx))
    else:
        b0.append((cd,idx))
    idx+=1
b12=b1+b2

print(b1)
print(b2)
print(b12)
thriples=[]
for b in b12:
    thriple=[]
    try:
        for i in range(b[1],b[1]+3):
            thriple.append(alfCad[i])
        #radix.radixSort(thriple)
        thriples.append((thriple,b[1]))
        #print(thriple)
        thriple=[]
    except:
        while(len(thriple)<3):
            thriple.append(0)
        thriples.append((thriple,b[1]))
        thriple=[]
        
print(thriples)

thriplesarray=[]
for th in thriples:
    thrip=''
    print(th)
    for t in th[0]:
        thrip+=str(t)
    thriplesarray.append(((int(thrip)),th[1]))
print(thriplesarray)

radix.radixSortTuple(thriplesarray)
print(thriplesarray)

tableRankThriple=[]
lastThr=(0,0)
currentRank=0
for thr in thriplesarray:
    if(thr[0]!=lastThr[0]):
        currentRank=currentRank+1
        tableRankThriple.append((thr,currentRank))
    else:
        tableRankThriple.append((thr,currentRank))
    lastThr=thr
print("-----")
print("-----")
print("-----")
print(tableRankThriple)


    
