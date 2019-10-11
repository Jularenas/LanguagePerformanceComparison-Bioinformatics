var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

var dna1='';
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
                //console.log(allText);
				dna1=allText
            }
        }
    }
    rawFile.send(null);
}

readTextFile1("file:///Users/Jularenas/Desktop/thesis/LanguagePerformanceComparison-Bioinformatics/performanceComparisonBioinformatics/javascript/fastaFiles/fasta_test5.fasta");
//console.log(dna1);

var fs = require('fs')
fs.appendFile('log.txt', 'new data', function (err) {
  if (err) {
    // append failed
  } else {
    // done
  }
})