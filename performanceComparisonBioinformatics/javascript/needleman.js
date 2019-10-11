var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var now = require("performance-now");
var dna1='';
var dna2='';
var cadena1='';
var cadena2='';
gap=2;
mut=1;
function readTextFile1(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
				dna1=allText;
				return allText;
            }
        }
    }
    rawFile.send(null);
}

function readTextFile2(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
				dna2=allText;
				return allText;
            }
        }
    }
    rawFile.send(null);
}
//readTextFile1('file:///Users/Jularenas/Desktop/thesis/jaascript/prueba1.fa')
//readTextFile2('file:///Users/Jularenas/Desktop/thesis/jaascript/prueba2.fa')

//console.log(dna1)
//console.log(dna2)

//var linesCad1 = dna1.split('\n');
//var linesCad2 = dna2.split('\n');


//for(var i =1;i<linesCad1.length;i++){
//	cadena1+=linesCad1[i]
//}

//for(var i =1;i<linesCad2.length;i++){
//	cadena2+=linesCad2[i]
//}
//console.log(cadena1)
//console.log(cadena2)
function dinamica (cadena1, cadena2){
	var matrizDinamica=new Array(cadena1.length+1)
	for(var i=0;i<matrizDinamica.length;i++){
		matrizDinamica[i]= new Array(cadena2.length+1)
	}
		
	//Llenar scores de los extremos
	for (var i = 0; i < matrizDinamica.length; i++) {
		matrizDinamica[i][0]=i*gap;
		//System.out.println(matrizDinamica[i][0]);
	}
	for (var i = 1; i < matrizDinamica[0].length; i++) {
		matrizDinamica[0][i]=i*gap	;
		//System.out.println(matrizDinamica[0][i]);
	}

	for (var i = 1; i < matrizDinamica.length; i++) {
		for (var j = 1; j < matrizDinamica[i].length; j++) {
			var upVal=matrizDinamica[i-1][j];
			var leftVal=matrizDinamica[i][j-1];
			var diagVal=matrizDinamica[i-1][j-1];
			
			var costUp=0;
			var costDiag=diagVal;
			var costLeft=0;
			
			costUp=upVal+gap;
			costLeft=leftVal+gap;
			if(!(cadena1.charAt(i-1)==cadena2.charAt(j-1))) {
				costDiag+=mut;
			}
			matrizDinamica[i][j]=Math.min(Math.min(costDiag, costLeft), costUp);
		}
	}
	score=matrizDinamica[cadena1.length][cadena2.length];
	//console.log(matrizDinamica)
	//console.log(cadena1.length)
	//console.log(cadena2.length)
	//console.log(score)
}

for(var i=5;i<13;i++){		
	readTextFile1("file:///Users/Jularenas/Desktop/thesis/LanguagePerformanceComparison-Bioinformatics/performanceComparisonBioinformatics/javascript/fastaFiles/fasta_test"+i+".fasta");
	for(var j=5;j<13;j++){
		readTextFile2("file:///Users/Jularenas/Desktop/thesis/LanguagePerformanceComparison-Bioinformatics/performanceComparisonBioinformatics/javascript/fastaFiles/fasta_test"+j+"_2.fasta");
		var start = now();
		dinamica(dna1,dna2);
		var end = now();
		var strTime=(end-start).toString();
		strTime=strTime.replace(".",",");
		var data=dna1.length+";"+dna2.length+";"+(strTime)+"\n";
		//console.log(dna1.length);
		//console.log(dna2.length);
		console.log(data);
		var fs = require('fs')
		fs.appendFileSync('javascriptResults.csv', data, function (err) {
		  if (err) {
			// append failed
		  } else {
			// done
		  }
		})
	}
}