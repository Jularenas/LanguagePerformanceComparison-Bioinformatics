package main

import (
    "fmt"
    "io/ioutil"
    "os"
	"log"
	"strings"
	"math"
	"strconv"
)
const gap float64=2
const mut float64=1

func main() {
	argsWithoutProg := os.Args[1:]

    file, err := os.Open("fastaFiles/"+argsWithoutProg[0])
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()


	b, err := ioutil.ReadAll(file)
	
	var cad1 string =string(b)

	file2, err2 := os.Open("fastaFiles/"+argsWithoutProg[1])
	if err2 != nil {
		log.Fatal(err2)
  	}
	defer file2.Close()
	

	b2, err2 := ioutil.ReadAll(file2)
	
	var cad2 string =string(b2)
	
	var dna1 string=""
	var dna2 string=""

	args1:=strings.Split(cad1,"\n")
	args2:=strings.Split(cad2,"\n")

	for index, element := range args1 {
		// index is the index where we are
		// element is the element from someSlice for where we are
		if index!=0{
			dna1= dna1+element
		}
	}
	
	for index, element := range args2 {
		// index is the index where we are
		// element is the s the element from someSlice for where we are
		if index!=0{
			dna2= dna2+element
		}
	}
	needleman(dna1,dna2)
  
}

func needleman(c1 string, c2 string){

	dy:=len(c1)+1
	dx:=len(c2)+1
	matrizDinamica := make([][]float64, dy)
	for i := range matrizDinamica {
    	matrizDinamica[i] = make([]float64, dx)
	}
	for i:=0;i<dy;i++{
		matrizDinamica[i][0]=gap*float64(i)
	}
	
	for i:=0;i<dx;i++{
		matrizDinamica[0][i]=gap*float64(i)
	}

	var upVal float64
	var leftVal float64
	var diagVal float64

	var costUp float64
	var costLeft float64
	var costDiag float64
	
	for i:=1;i<dy;i++{
		for j:=1;j<dx;j++{
			upVal=matrizDinamica[i-1][j]
			leftVal=matrizDinamica[i][j-1]
			diagVal=matrizDinamica[i-1][j-1]

			costUp=float64(upVal+gap)
			costLeft=float64(leftVal+gap)
			costDiag=float64(diagVal)
			if(c1[i-1]!=c2[j-1]){
				costDiag=costDiag+mut
			}
			matrizDinamica[i][j]=math.Min(math.Min(costDiag,costUp),costLeft)
		}
	}

	for i:=1;i<dy;i++{
		var cadPr string =""
		for j:=1;j<dx;j++{
			cadPr= cadPr+FloatToString(matrizDinamica[i][j])+"  "
		}
		//fmt.Println(cadPr)
	}
	fmt.Println(c1)
	fmt.Println(c2)
	fmt.Println(matrizDinamica[dy-1][dx-1])
}
func FloatToString(input_num float64) string {
    // to convert a float number to a string
    return strconv.FormatFloat(input_num, 'f', 6, 64)
}
