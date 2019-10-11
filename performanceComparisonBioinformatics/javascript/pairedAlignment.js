var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var now = require("performance-now");
var dna1='';
var dna2='';
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

function dinamica (cadena1, cadena2){
	var matrizDinamica=new Array(cadena1.length+1)
	for(var i=0;i<matrizDinamica.length;i++){
		matrizDinamica[i]= new Array(cadena2.length+1)
	}
		
	//Llenar scores de los extremos
	for (var i = 0; i < matrizDinamica.length; i++) {
		matrizDinamica[i][0]=i*gap;
	}
	for (var i = 1; i < matrizDinamica[0].length; i++) {
		matrizDinamica[0][i]=i*gap	;
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
	console.log(score)
}

var myArgs = process.argv.slice(2);
readTextFile1("file:///Users/Jularenas/Desktop/thesis/LanguagePerformanceComparison-Bioinformatics/performanceComparisonBioinformatics/javascript/fastaFiles/"+myArgs[0]);
readTextFile2("file:///Users/Jularenas/Desktop/thesis/LanguagePerformanceComparison-Bioinformatics/performanceComparisonBioinformatics/javascript/fastaFiles/"+myArgs[1]);

var d1=dna1.split("\n");
var d2=dna2.split("\n");
var cad1="";
var cad2="";
for(var i=0;i<d1.length;i++){
	cad1+=d1[i];
}
for(var i=0;i<d2.length;i++){
	cad2+=d2[i];
}
//console.log(cad1);
//console.log(cad2);
dinamica(cad1,cad2);
