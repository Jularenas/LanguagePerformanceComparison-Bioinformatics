import rank
import radix
stringTry='yabbadabbado'
k=2
#Create sample sets
sets = [[] for i in range(k+1)]
#print (sets)

m=0
for i, character in enumerate(stringTry):
    #print(sets)
    #print(c)
    #print(m%(k+1))
    sets[m%(k+1)].append(i)
    m+=1
print("subsets")
print(sets)

idx=0

#Set of sample suffixes
c=[]
for i in range(k+1):
    if(idx==0):
        idx+=1
    else:
        c+=sets[i]
print("C: sample suffixes")
print(c)

#sort sample suffixes


#construct strings r1..rk
sampleString=[]
for i in range(1,k+1):
    #s=[[]for j in range(len(stringTry)/k)]
    ss=[]
    count=1
    st=''
    for m in range(i,len(stringTry)+k):
        try:
            st+=stringTry[m]
            if (count%3==0 ):
                ss.append(st)
                st=''
            count+=1
        except:
            st+='0'
            if (count%3==0 ):
                ss.append(st)
                st=''
            count+=1
    sampleString.append(ss)
print("sampleString")
#print(sampleString)
sampleS=[]
for s in sampleString:
    sampleS+=s
print(sampleS)

#Obtaining R'
rPrime=[]
for s in sampleS:
    if('0'in s):
        rPrime.append(rank.findRank(s)+k)
    else:
        rPrime.append(rank.findRank(s))
print (rPrime)

#obtaining SA'

#rPrimeFix=[[rPrime[0],rPrime.index(rPrime[0])]]
rPrimeFix=[]
idx=0
for rp in rPrime:
    x=[rp,rPrime.index(rp,idx)]
    rPrimeFix.append(x)
    idx+=1

#print(rPrimeFix)

result=radix.radixSort(rPrimeFix)
print(result)

saPrime=[]
saPrime.append(len(result))
for rs in result:
    saPrime.append(rs[1])
print("SA'",saPrime)
        

