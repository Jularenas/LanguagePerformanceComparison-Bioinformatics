package main

    //"io/ioutil"
    //"os"
	//"log"
	//"strings"
	//"math"
import (
    "fmt"
	"strconv"
)


// Finds the largest number in an array
func findLargestNum(array []int) int {
	largestNum := 0

	for i := 0; i < len(array); i++ {
		if array[i] > largestNum {
			largestNum = array[i]
		}
	}
	return largestNum
}

// Radix Sort
func radixSort(array []int) []int {

  //fmt.Println("Running Radix Sort on Unsorted List\n")

  // Base 10 is used
	largestNum := findLargestNum(array)
	size := len(array)
	significantDigit := 1
	semiSorted := make([]int, size, size)

	// Loop until we reach the largest significant digit
	for largestNum / significantDigit > 0 {
  
    //fmt.Println("\tSorting: " + strconv.Itoa(significantDigit) + "'s place", array)

		bucket := [10]int{0}

		// Counts the number of "keys" or digits that will go into each bucket
		for i := 0; i < size; i++ {
			bucket[(array[i] / significantDigit) % 10]++
		}

		// Add the count of the previous buckets
    // Acquires the indexes after the end of each bucket location in the array
		// Works similar to the count sort algorithm
		for i := 1; i < 10; i++ {
			bucket[i] += bucket[i - 1] 
		}

		// Use the bucket to fill a "semiSorted" array
		for i := size - 1; i >= 0; i-- {
			bucket[(array[i] / significantDigit) % 10]--
			semiSorted[bucket[(array[i] / significantDigit) % 10]] = array[i]
		}

    // Replace the current array with the semisorted array
		for i := 0; i < size; i++ {
			array[i] = semiSorted[i]
		}
    
    //fmt.Println("\n\tBucket: ", bucket)
  
    // Move to next significant digit
		significantDigit *= 10 
	}

	return array
}

func main() {

  //fmt.Println("\n\nRunning Radix Sort Example in Go!")
  //fmt.Println("----------------------------------\n")

	//unsortedList :=[]int{10, 2, 303, 4021, 293, 1, 0, 429, 480, 92, 2999, 14}
	//fmt.Println("Unsorted List:", unsortedList, "\n")

	//sortedList := radixSort(unsortedList)

	//fmt.Println("\nSorted List:", sortedList, "\n")

	cadena :="yabbadabbado"
	var resultado[]int
	resultado=dc3(cadena)
	fmt.Println(resultado)
}

func dc3(cad string)[]int{
	//construccion alfabeto
	cadLen:=len(cad)
	alf:=make([]int, cadLen)

	fmt.Println("cadLength",cadLen)

	//isRecursiveStep
	var isNumber=false
	if _, err := strconv.Atoi(cad); err == nil {
		fmt.Printf("%q looks like a number.\n", cad)
		isNumber=true
	}

	if isNumber{
		for pos, char := range cad {
			//fmt.Printf("character %c starts at byte position %d\n", char, pos)
			alf[pos]=int(char-'0')
		}
	}else{
		for pos, char := range cad {
			//fmt.Printf("character %c starts at byte position %d\n", char, pos)
			alf[pos]=int(char)
		}
	}

	radixSort(alf)
	fmt.Println("sorted alf",alf)
	var alfDict map [string]int
	alfDict=make( map [string]int)
	
	if(isNumber){
		fmt.Println("is a number")
		for index, element := range alf {
			// index is the index where we are
			// element is the element from someSlice for where we are
			s:= strconv.Itoa(element)
			i, err := strconv.Atoi(s)
			fmt.Println(index,err)
			alfDict[s]=i
		}
	} else{
		fmt.Println("is not a number")
		var lastChar=-1
		var idx=0
		for index, element := range alf {
			// index is the index where we are
			// element is the element from someSlice for where we are
			if(lastChar!=element){
				idx=idx+1
				s:= string(rune(element))
				alfDict[s]=idx
				fmt.Println(index)
			}
			lastChar=element
		}
	}

	fmt.Println(alfDict)

	alfCad:=make([]int,cadLen+1)


	for pos, char := range cad {
		//fmt.Printf("character %c starts at byte position %d\n", char, pos)
		fmt.Println(string(char))
		alfCad[pos]=alfDict[string(char)]
	}
	alfCad[cadLen]=0
	fmt.Println(alfCad)
	//for key, value := range alfCad {
	//	fmt.Println("Key:", key, "Value:", value)
	//}	

	//Crear sample set y b0

	var b0 [][]int
	var b1 [][]int
	var b2 [][]int
	var b12 [][]int
	var idx int=0
	for idx<len(alfCad){
		if idx%3==1{
			tuple :=[...]int {alfCad[idx],idx}
			tuple1:=tuple[:] 
			b1=append(b1,  tuple1 )
		}else if (idx%3==2){
			tuple :=[...]int {alfCad[idx],idx}
			tuple1:=tuple[:] 
			b2=append(b2,  tuple1 )
		}else{
			tuple :=[...]int {alfCad[idx],idx}
			tuple1:=tuple[:] 
			b0=append(b0,  tuple1 )
		}
		idx+=1
	}
	fmt.Println(b1)
	fmt.Println(b2)
	fmt.Println(b0)

	var i int =0
	for i<len(b1){
		b12=append(b12,b1[i])
		i+=1
	}

	i=0
	for i<len(b2){
		b12=append(b12,b2[i])
		i+=1
	}
	fmt.Println(b12)

	var thriples [][]int

	i=0
	for i<len(b12){	
		var currentb12 []int=b12[i]
		//fmt.Println(currentb12)
		if currentb12[1]!=(len(alfCad)-1){
			fmt.Println(currentb12)
			if (currentb12[1]+3)<len(alfCad){
				var j int=currentb12[1]
				var jC int=j+3
				var st string=""
				for j<jC{
					s:=strconv.Itoa(alfCad[j])
					st+=s
					j+=1
				}
				inti,err:=strconv.Atoi(st)
				fmt.Println("thriple")
				tuple :=[...]int {inti,currentb12[1]}
				tuple1:=tuple[:] 
				thriples=append(thriples,  tuple1 )
				fmt.Println(inti)
				fmt.Println(err)
				fmt.Println("b[1]")
				fmt.Println(currentb12[1])
				//tuple :=[...]int {thriple,b[1]}
				//tuple1:=tuple[:] 
			}else{
				var j int=currentb12[1]
				var st string=""
				for j<len(alfCad){
					s:=strconv.Itoa(alfCad[j])
					st+=s
					j+=1
				}
				for len(st)<3{
					s:=strconv.Itoa(0)
					st+=s
					j+=1
				}
				inti,err:=strconv.Atoi(st)
				tuple :=[...]int {inti,currentb12[1]}
				tuple1:=tuple[:] 
				thriples=append(thriples,  tuple1 )
				fmt.Println(err)
			}
		}
	i+=1
	}
	fmt.Println(thriples)
	
	sortedTuples:=radixSortTuple(thriples)
	fmt.Println(sortedTuples)
	var lastThr []int
	lastThr=make([]int,2)
	var b12IndexRank map [string]int
	var currentRank int
	var duplicates=false
	currentRank=0
	b12IndexRank=make( map [string]int)

	i=0
	for i<2{
		lastThr[i]=-1
		i+=1
	}

	i=0
	for i<len(thriples){
		if (thriples[i][0])!=(lastThr[0]){
			fmt.Println("firstIF")
			currentRank+=1
			stKey:=strconv.Itoa(thriples[i][1])
			b12IndexRank[stKey]=currentRank
		}else{
			fmt.Println("secondIF")
			stKey:=strconv.Itoa(thriples[i][1])
			b12IndexRank[stKey]=currentRank
            duplicates=true
		}
		lastThr=thriples[i]
		i+=1
	}

	stKeyF:=strconv.Itoa(len(cad))
	stKeyF1:=strconv.Itoa(len(cad)+1)
	stKeyF2:=strconv.Itoa(len(cad)+2)
    b12IndexRank[stKeyF]=0
    b12IndexRank[stKeyF1]=0
	b12IndexRank[stKeyF2]=0

	fmt.Println(b12IndexRank)
	var b0Tuples21 [][]int

	
	if duplicates{
		var newArray[]int
		newArray=make([]int,len(thriples)+2)
		i=0
		for i<len(b12){
			stb12:=strconv.Itoa(b12[i][1])
			newArray[i]=b12IndexRank[stb12]
			i+=1
		} 
		newArray[len(thriples)]=0
		newArray[len(thriples)+1]=0

		i=0
		var stNew=""
		for i<len(newArray) {
			sN:=strconv.Itoa(newArray[i])
			stNew+=sN
			i+=1
		}
		fmt.Println(stNew)
		//Recursive call


		var recReturn []int
		recReturn=dc3(stNew)

		fmt.Println("-----returned array------")
		fmt.Println(recReturn)

		var sortedB12 [][]int
		sortedB12=make([][]int,len(b12))

		i=1
		for i<len(recReturn){
			var b12val []int
			b12val=b12[recReturn[i]]
			sortedB12[i-1]=b12val
			i+=1
		} 

		i=0
		for i<len(sortedB12){
			sSorted:=strconv.Itoa(sortedB12[i][1])
			b12IndexRank[sSorted]=i+1
			i+=1
		}

		fmt.Println(b12IndexRank)

		i=0
		for i<len(b0){
			var intB int
			intB=b12IndexRank[strconv.Itoa(b0[i][1]+1)]
			var stringB string
			stringB=strconv.Itoa(intB)
			//fmt.Println(stringB)
			strB0:=strconv.Itoa(b0[i][0])
			t1,err:=strconv.Atoi(strB0+stringB)
			tuple :=[...]int {t1,b0[i][1]}
			tuple1:=tuple[:] 
			b0Tuples21=append(b0Tuples21,tuple1)
			fmt.Println(err)
			i=i+1
		}
		fmt.Println("------b0------")
		fmt.Println(b0Tuples21)
		b0Tuples21=radixSortTuple(b0Tuples21)

		
		fmt.Println("------b0Sorted------")
		fmt.Println(b0Tuples21)

		var result []int

		result=make([]int,0)


		var idx int
		var idx2 int
		idx=0
		idx2=0
		for (idx<len(b0Tuples21)&&idx2<len(sortedB12)){
			for (idx2<len(sortedB12) && idx<len(b0Tuples21)){
				var idxB0 int
				var idxB12 int
				idxB0=b0Tuples21[idx][1]
				idxB12=sortedB12[idx2][1]
				fmt.Println("idxB0",idxB0)
				fmt.Println("idxB12",idxB12)
				if idxB12%3==2{
					var charB12 int
					var charB0 int
					charB12=alfCad[idxB12]
					charB0=alfCad[idxB0]
					if charB0>charB12{
						result=append(result,idxB12)
						idx2+=1
					}else if charB0<charB12 {
						result=append(result,idxB0)
						idx+=1
					}else{
						var charB12P1 int
						var charB0P1 int
						charB12P1=alfCad[idxB12+1]
						charB0P1=alfCad[idxB0+1]
						if charB0P1>charB12P1{
							result=append(result,idxB12)
							idx2+=1
						}else if charB12P1>charB0P1{
							result=append(result,idxB0)
							idx+=1	
						}else{
							strIdxB0P2:=strconv.Itoa(idxB0+2)
							strIdxB12P2:=strconv.Itoa(idxB12+2)
							var rankB0P2 int
							var  rankB12P2 int
							rankB0P2=b12IndexRank[strIdxB0P2]
							rankB12P2=b12IndexRank[strIdxB12P2]
							if rankB0P2>rankB12P2{
								result=append(result,idxB12)
								idx2+=1
							}else{
								result=append(result,idxB0)
								idx+=1	
							}
						}
					}
				}else if idxB12%3==1{
					var charB12 int
					var charB0 int
					charB12=alfCad[idxB12]
					charB0=alfCad[idxB0]
					
//					fmt.Println("charB12",charB12)
//					fmt.Println("charB0",charB0)

					if charB0>charB12{
						result=append(result,idxB12)
						idx2+=1
					}else if charB0<charB12{
						result=append(result,idxB0)
						idx+=1
					}else{
						strIdxB0P1:=strconv.Itoa(idxB0+1)
						strIdxB12P1:=strconv.Itoa(idxB12+1)
						var rankB0P1 int
						var  rankB12P1 int
						rankB0P1=b12IndexRank[strIdxB0P1]
						rankB12P1=b12IndexRank[strIdxB12P1]
						if rankB0P1>rankB12P1{
							result=append(result,idxB12)
							idx2+=1
						}else{
							result=append(result,idxB0)
							idx+=1	
						}
					}
				}
			}
		}

		if (idx>=len(thriples) && idx2!=len(b0Tuples21)){
			i=idx
			for i<len(b0Tuples21){
				result=append(result,b0Tuples21[i][1])
				i+=1
			} 
		}else if (idx!=len(thriples) && idx2>=len(b0Tuples21)){
			i=idx2
			for i<len(thriples){
				result=append(result,thriples[i][1])
				i+=1
			} 
		}
		return result

	}else{
		fmt.Println("-------non duplicates-------")
		fmt.Println(b0)
		if len(b0) > 0 {
			b0 = b0[:len(b0)-1]
		}

		i=0
		for i<len(b0){
			var intB int
			intB=b12IndexRank[strconv.Itoa(b0[i][1]+1)]
			var stringB string
			stringB=strconv.Itoa(intB)
			//fmt.Println(stringB)
			strB0:=strconv.Itoa(b0[i][0])
			t1,err:=strconv.Atoi(strB0+stringB)
			tuple :=[...]int {t1,b0[i][1]}
			tuple1:=tuple[:] 
			b0Tuples21=append(b0Tuples21,tuple1)
			fmt.Println(err)
			i=i+1
		}
		fmt.Println("------b0------")
		fmt.Println(b0Tuples21)
		b0Tuples21=radixSortTuple(b0Tuples21)

		
		fmt.Println("------b0Sorted------")
		fmt.Println(b0Tuples21)
		var result[]int
		fmt.Println("------lenOfResult----- ")
		fmt.Println(len(b0Tuples21)+len(b12))
		result=make([]int,0)


		var idx int
		var idx2 int
		idx=0
		idx2=0
		for (idx<len(b0Tuples21)&&idx2<len(thriples)){
			for (idx2<len(thriples) && idx<len(b0Tuples21)){
				var idxB0 int
				var idxB12 int
				idxB0=b0Tuples21[idx][1]
				idxB12=thriples[idx2][1]
				fmt.Println("idxB0",idxB0)
				fmt.Println("idxB12",idxB12)
				if idxB12%3==2{
					var charB12 int
					var charB0 int
					charB12=alfCad[idxB12]
					charB0=alfCad[idxB0]
					if charB0>charB12{
						result=append(result,idxB12)
						idx2+=1
					}else if charB0<charB12 {
						result=append(result,idxB0)
						idx+=1
					}else{
						var charB12P1 int
						var charB0P1 int
						charB12P1=alfCad[idxB12+1]
						charB0P1=alfCad[idxB0+1]
						if charB0P1>charB12P1{
							result=append(result,idxB12)
							idx2+=1
						}else if charB12P1>charB0P1{
							result=append(result,idxB0)
							idx+=1	
						}else{
							strIdxB0P2:=strconv.Itoa(idxB0+2)
							strIdxB12P2:=strconv.Itoa(idxB12+2)
							var rankB0P2 int
							var  rankB12P2 int
							rankB0P2=b12IndexRank[strIdxB0P2]
							rankB12P2=b12IndexRank[strIdxB12P2]
							if rankB0P2>rankB12P2{
								result=append(result,idxB12)
								idx2+=1
							}else{
								result=append(result,idxB0)
								idx+=1	
							}
						}
					}
				}else if idxB12%3==1{
					var charB12 int
					var charB0 int
					charB12=alfCad[idxB12]
					charB0=alfCad[idxB0]
					
//					fmt.Println("charB12",charB12)
//					fmt.Println("charB0",charB0)

					if charB0>charB12{
						result=append(result,idxB12)
						idx2+=1
					}else if charB0<charB12{
						result=append(result,idxB0)
						idx+=1
					}else{
						strIdxB0P1:=strconv.Itoa(idxB0+1)
						strIdxB12P1:=strconv.Itoa(idxB12+1)
						var rankB0P1 int
						var  rankB12P1 int
						rankB0P1=b12IndexRank[strIdxB0P1]
						rankB12P1=b12IndexRank[strIdxB12P1]
						if rankB0P1>rankB12P1{
							result=append(result,idxB12)
							idx2+=1
						}else{
							result=append(result,idxB0)
							idx+=1	
						}
					}
				}
			}
		}

		if (idx>=len(thriples) && idx2!=len(b0Tuples21)){
			i=idx
			for i<len(b0Tuples21){
				result=append(result,b0Tuples21[i][1])
				i+=1
			} 
		}else if (idx!=len(thriples) && idx2>=len(b0Tuples21)){
			i=idx2
			for i<len(thriples){
				result=append(result,thriples[i][1])
				i+=1
			} 
		}
		return result
	}
	return nil
}


func radixSortTuple(array [][]int) [][]int {

	//fmt.Println("Running Radix Sort on Unsorted List\n")
  
	// Base 10 is used
	  largestNum := findLargestNum(array[0])
	  size := len(array)
	  significantDigit := 1
	  semiSorted := make([][]int, size, size)
  
	  // Loop until we reach the largest significant digit
	  for largestNum / significantDigit > 0 {
	
	  //fmt.Println("\tSorting: " + strconv.Itoa(significantDigit) + "'s place", array)
  
		  bucket := [10]int{0}
  
		  // Counts the number of "keys" or digits that will go into each bucket
		  
		  for i := 0; i < size; i++ {
			  
			  fmt.Println(array[i][0])
			  bucket[(array[i][0] / significantDigit) % 10]++
		  }
  
		  // Add the count of the previous buckets
	  // Acquires the indexes after the end of each bucket location in the array
		  // Works similar to the count sort algorithm
		  for i := 1; i < 10; i++ {
			  bucket[i] += bucket[i - 1] 
		  }
  
		  // Use the bucket to fill a "semiSorted" array
		  for i := size - 1; i >= 0; i-- {
			  bucket[(array[i][0] / significantDigit) % 10]--
			  semiSorted[bucket[(array[i][0] / significantDigit) % 10]] = array[i]
		  }
  
	  // Replace the current array with the semisorted array
		  for i := 0; i < size; i++ {
			  array[i] = semiSorted[i]
		  }
	  
	  //fmt.Println("\n\tBucket: ", bucket)
	
	  // Move to next significant digit
		  significantDigit *= 10 
	  }
  
	  return array
  }
  