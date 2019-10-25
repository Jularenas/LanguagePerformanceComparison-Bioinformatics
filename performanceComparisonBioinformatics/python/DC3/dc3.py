import pdb
import radix

specialChar='0'

def dc3(cad):
    #cadena
    print("--------Cadena--------")
    print("--------Cadena--------",cad)
    print("--------Cadena--------")
    #construccion de alfabeto
    
    alf=[]
    for c in cad:
        alf.append(ord(c))
    #print(alf)

    radix.radixSort(alf)

    #print(alf)
    alfDict={}
    try:
        float(cad)
        for a in alf:
            alfDict[chr(a)]=int(chr(a))
        print(alfDict)
    except:
        index=0
        lastChar=-1
        for a in alf:
            if(a != lastChar):
                index+=1
                alfDict[chr(a)]=index
            lastChar=a
        print(alfDict)
                
    alfCad=[]
    for c in cad:
        print(c)
        alfCad.append(alfDict[c])
    alfCad.append(0)
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
    print("----B12-----")
    print(b12)
    thriples=[]
    for b in b12:
        thriple=[]
        if(b[1]!=(len(alfCad)-1)):
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
    print("----Thriples-----")
    print(thriples)

    thriplesarray=[]
    for th in thriples:
        thrip=''
        #print(th)
        for t in th[0]:
            thrip+=str(t)
        thriplesarray.append(((int(thrip)),th[1]))
    print("---thriplesarray---")
    print(thriplesarray)

    radix.radixSortTuple(thriplesarray)
    print("---thriplesarraySorted---")
    print(thriplesarray)

    tableRankThriple=[]
    lastThr=(-1,-1)
    currentRank=0
    b12IndexRank={}
    duplicates=False
    for thr in thriplesarray:
        if(thr[0]!=lastThr[0]):
            currentRank=currentRank+1
            tableRankThriple.append((thr,currentRank))
            b12IndexRank[str(thr[1])]=currentRank
        else:
            tableRankThriple.append((thr,currentRank))
            b12IndexRank[str(thr[1])]=currentRank
            duplicates=True
        lastThr=thr
    b12IndexRank[str(len(cad))]=0
    b12IndexRank[str(len(cad)+1)]=0
    b12IndexRank[str(len(cad)+2)]=0
    print("-----")
    print("-----")
    print("--Table Rank thriple--")
    print(tableRankThriple)
    #b0Tuples=[]
    #b0Tuples2=[]
    b0Tuples21=[]
    if(duplicates):
        newArray=[0]*(len(tableRankThriple)+2)

        print("----indexRank---")
        print(b12IndexRank)
        for i in range(0,len(b12)+2):
            try:
                print(b12[i][1])
                newArray[i]=b12IndexRank[str(b12[i][1])]
            except Exception as e:
                #print(e)
                print(i)
                newArray[i]=0
                continue
        print("array for recursion")
        print(newArray)
        st=''
        for a in newArray:
            st+=str(a)



        #recursive call
            
        recReturn=dc3(st)
        print("returned")
        print(recReturn)

        print("dict",b12IndexRank)

        sortedB12=[0]*len(b12)
        for i in range(1,len(recReturn)):
            b12Val=b12[recReturn[i]]
            sortedB12[i-1]=b12Val

        print("sortedB12",sortedB12)

        print("pretrans",b12IndexRank)
    
        for i in range(0,len(sortedB12)):
            b12IndexRank[str(sortedB12[i][1])]=i+1
        print(b12IndexRank["5"])
        



        print("posTrans",b12IndexRank) 
        print("---b0---")
        print(b0)
        for b in b0:
            intB=b12IndexRank[str((b[1]+1))]
            print(intB,str((b[1]+1)))
            stringB=str(intB)
            #b0Tuples.append(int(stringB+str(b[0])))
            #b0Tuples2.append((intB,b[0]))
            #print(stringB)
            b0Tuples21.append((int(str(b[0])+stringB),((b[0],intB),b[1])))
        #radix.radixSort(b0Tuples)
        #radix.radixSortTuple(b0Tuples2)
        print("---b0unSorted--")
        print(b0Tuples21)
        print("---b0Sorted--")
        radix.radixSortTuple(b0Tuples21)
        #print(b0Tuples)
        #print(b0Tuples2)
        print(b0Tuples21)

        result=[]
        idx=0
        idx2=0
        while(idx<len(b0Tuples21)and idx2<len(sortedB12)):
            while(idx2<len(sortedB12) and idx<len(b0Tuples21)):              
                currentB0=b0Tuples21[idx]
                idxB0=currentB0[1][1]
                print(idx,idx2)
                currentB12=sortedB12[idx2]
                idxB12=currentB12[1]
                #print("idx%3",idxB12%3)
                if(idxB12%3==2):
                    charB12=alfCad[idxB12]
                    charB0=alfCad[idxB0]
                    #print(charB12,charB0)
                    if(charB0>charB12):
                        result.append(idxB12)
                        idx2=idx2+1
                        print("bien")
                    elif(charB0<charB12):
                        result.append(idxB0)
                        idx=idx+1
                    else:
                        charB12P1=alfCad[idxB12+1]
                        charB0P1=alfCad[idxB0+1]
                        if(charB0P1>charB12P1):
                            result.append(idxB12)
                            idx2=idx2+1
                        elif(charB0P1<charB12P1):
                            result.append(idxB0)
                            idx=idx+1
                        else:
                            rankB0P2=b12IndexRank[str(idxB0+2)]
                            rankB12P2=b12IndexRank[str(idxB12+2)]
                            if(rankB0P2>rankB12P2):
                                result.append(idxB12)
                                idx2=idx2+1
                            elif(rankB0P2<rankB12P2):
                                result.append(idxB0)
                                idx=idx+1
                            else:
                                print("error")
                elif(idxB12%3==1):
                    currentB12=tableRankThriple[idx2]
                    idxB12=currentB12[0][1]
                    charB12=alfCad[idxB12]
                    charB0=alfCad[idxB0]
                    #print("charB0",charB0)
                    print("charB0-charB12",charB0,charB12)
                    print("idxB12",idxB12)
                    if(charB0>charB12):
                        result.append(idxB12)
                        idx2=idx2+1
                    elif(charB0<charB12):
                        result.append(idxB0)
                        idx=idx+1
                    else:
                        rankB0P1=b12IndexRank[str(idxB0+1)]
                        rankB12P1=b12IndexRank[str(idxB12+1)]
                        print("rankB0-rankrB12",rankB0P1,rankB12P1)
                        if(rankB0P1>rankB12P1):
                            result.append(idxB12)
                            idx2=idx2+1
                        elif(rankB0P1<rankB12P1):
                            print("idxB0",idxB0)
                            result.append(idxB0)
                            idx=idx+1
                        else:
                            print(recReturn)
            pdb.set_trace()
        #DeadCode?
        print("aaaaaaaaaaaa")
        
        print("----indices finales-----------",idx,idx2)
            
        if(idx>=len(tableRankThriple)and idx2!=len(b0Tuples21)):
            for i in range(idx,len(b0Tuples21)):
                currentB0=b0Tuples21[i]
                idxB0=currentB0[1][1]
                result.append(idxB0)
        elif(idx!=len(tableRankThriple)and idx2>=len(b0Tuples21)):
            print("---HELP--")
            for i in range(idx2,len(tableRankThriple)):
                currentB12=tableRankThriple[i]
                idxB12=currentB12[0][1]
                result.append(idxB12)
            #if(idx2==len(tableRankThriple) and idx<len(b0Tuples21)):
            #    break
        print(result)
        return(result)
    else:
        print("----indexRank---")
        print(b12IndexRank)
        b0.pop()
        print("---b0---")
        print(b0)
        for b in b0:
            intB=b12IndexRank[str((b[1]+1))]
            stringB=str(intB)
            #b0Tuples.append(int(stringB+str(b[0])))
            #b0Tuples2.append((intB,b[0]))
            b0Tuples21.append((int(str(b[0])+stringB),((b[0],intB),b[1])))
        #radix.radixSort(b0Tuples)
        #radix.radixSortTuple(b0Tuples2)
        radix.radixSortTuple(b0Tuples21)
        
        print("---b0Sorted--")
        #print(b0Tuples)
        #print(b0Tuples2)
        print(b0Tuples21)
        
        result=[]
        idx=0
        idx2=0
        while(idx<len(b0Tuples21)and idx2<len(tableRankThriple)):
            while(idx2<len(tableRankThriple) and idx<len(b0Tuples21)):
                currentB0=b0Tuples21[idx]
                idxB0=currentB0[1][1]
                print(idx,idx2)
                currentB12=tableRankThriple[idx2]
                idxB12=currentB12[0][1]
                print("idx%3",idxB12%3)
                if(idxB12%3==2):
                    charB12=alfCad[idxB12]
                    charB0=alfCad[idxB0]
                    print("charB12-B0",charB12,charB0)
                    if(charB0>charB12):
                        result.append(idxB12)
                        idx2=idx2+1
                    elif(charB0<charB12):
                        result.append(idxB0)
                        idx=idx+1
                    else:
                        charB12P1=alfCad[idxB12+1]
                        charB0P1=alfCad[idxB0+1]
                        print("charB12P1-B0P1",charB12P1,charB0P1)
                        if(charB0P1>charB12P1):
                            result.append(idxB12)
                            idx2=idx2+1
                        elif(charB0P1<charB12P1):
                            result.append(idxB0)
                            idx=idx+1
                        else:
                            rankB0P2=b12IndexRank[str(idxB0+2)]
                            rankB12P2=b12IndexRank[str(idxB12+2)]
                            if(rankB0P2>rankB12P2):
                                result.append(idxB12)
                                idx2=idx2+1
                            elif(rankB0P2<rankB12P2):
                                result.append(idxB0)
                                idx=idx+1
                            else:
                                print("error")
                elif(idxB12%3==1):
                    currentB12=tableRankThriple[idx2]
                    idxB12=currentB12[0][1]
                    charB12=alfCad[idxB12]
                    charB0=alfCad[idxB0]
                    #print("charB0",charB0)
                    print("charB0-charB12",charB0,charB12)
                    if(charB0>charB12):
                        result.append(idxB12)
                        idx2=idx2+1
                    elif(charB0<charB12):
                        result.append(idxB0)
                        idx=idx+1
                    else:
                        rankB0P1=b12IndexRank[str(idxB0+1)]
                        rankB12P1=b12IndexRank[str(idxB12+1)]
                        print("rankB0-rankrB12",rankB0P1,rankB12P1)
                        if(rankB0P1>rankB12P1):
                            result.append(idxB12)
                            idx2=idx2+1
                            print("verifySize",idx2,len(tableRankThriple))
                        elif(rankB0P1<rankB12P1):
                            print("idxB0",idxB0)
                            result.append(idxB0)
                            idx=idx+1
                        else:
                            print("alo")
           
        print("aaaaaaaaaaaa")
        
        print("----indices finales-----------",idx,idx2)
            
        if(idx>=len(tableRankThriple)and idx2!=len(b0Tuples21)):
            for i in range(idx,len(b0Tuples21)):
                currentB0=b0Tuples21[i]
                idxB0=currentB0[1][1]
                result.append(idxB0)
        elif(idx!=len(tableRankThriple)and idx2>=len(b0Tuples21)):
            print("---HELP--")
            for i in range(idx2,len(tableRankThriple)):
                currentB12=tableRankThriple[i]
                idxB12=currentB12[0][1]
                result.append(idxB12)
            #if(idx2==len(tableRankThriple) and idx<len(b0Tuples21)):
            #    break
        print(result)
        return(result)
        print(result)
        return result
                
        



cad1='ATTTAGGATT'
sa=dc3(cad1)
for s in sa:
    print(s,cad1[s:len(cad1)])
