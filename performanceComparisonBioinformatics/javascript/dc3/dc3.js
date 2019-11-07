
//Radix functions
function getMax(arr) {

    let max = 0;
    for (let num of arr) {
        if (max < num.toString().length) {
            max = num.toString().length
        }
    }
    return max
}

function getPosition(num, place){
 return  Math.floor(Math.abs(num)/Math.pow(10,place))% 10
}

function radixSort(arr) {

    const max = getMax(arr); // length of the max digit in the array

    for (let i = 0; i < max; i++) {
        let buckets = Array.from({ length: 10 }, () => [ ])
        for (let j = 0; j < arr.length; j++) {
          buckets[getPosition(arr[ j ], i)].push(arr[ j ]); // pushing into buckets
        }
        arr = [ ].concat(...buckets);
    }
    return arr
}
//End radix functions

//var specialChar='0';

function dc3(cad){
	
	//construcción del alfabeto
	var alf=[];
	for(var i=0;i<cad.length;i++){
		alf.push(cad.charCodeAt(i));
	}
	
	//console.log(alf)
	alf=radixSort(alf);
	//console.log(alf)
	
	var alfDict={};
		var intCad=parseInt(cad)
		
		if(!(Number.isNaN(intCad))){			
			for(var i=0;i<alf.length;i++){
				alfDict[String.fromCharCode(alf[i])]=parseInt(String.fromCharCode(alf[i]));
			} 	
		}
		else{
			var index=0;
			var lastChar=-1
			for(var i=0; i<alf.length;i++){
				var a=alf[i];
				if(a!=lastChar){
					index+=1;
					alfDict[String.fromCharCode(alf[i])]=index;
				}
				lastChar=a;
			}
		}
	console.log(alfDict);
	alfCad=[];
	for(var i=0;i<cad.length;i++){
		alfCad.push(alfDict[cad.charAt(i)]);
	}
	alfCad.push(0);
	//console.log(alfCad);
	
	
	//SAmple set
	
	var b1=[];
	var b2=[];
	var b0=[];
	var b12idx=[];
	var idx=0;
	
	for(var i=0; i<alfCad.length;i++){
		if(idx%3==1){
			b1.push([alfCad[i],idx]);
		}
		else if(idx%3==2){
			b2.push([alfCad[i],idx]);
		}
		else{
			b0.push([alfCad[i],idx]);
		}
		idx+=1;
	}
	var b12=b1.concat(b2);
	
	console.log(b12);
	
	thriples=[];
	for(var i=0;i<b12.length;i++){
		var thriple=[];
		var currentb=b12[i];
		console.log(currentb)
		if(currentb[1]!=(alfCad.length-1)){
				for(var j=currentb[1];j<currentb[1]+3;j++){
					if(alfCad[j]!=undefined){
						thriple.push(alfCad[j]);	
					}
					else{
						thriple.push(0);
					}
				}
				thriples.push([thriple,currentb[1]]);
				thriple=[];
		}
	}
	console.log(thriples);
	
	thriplesArray=[];
	
	
}

var cadena="YABBADABADO"

dc3(cadena);