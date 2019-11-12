
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

function radixSortTuple(arr) {

	var arra=[];
	for(var i=0;i<arr.length;i++){
		arra.push(arr[i][0]);
	}
    const max = getMax(arra); // length of the max digit in the array

    for (let i = 0; i < max; i++) {
        let buckets = Array.from({ length: 10 }, () => [ ])
		//console.log(buckets);
        for (let j = 0; j < arr.length; j++) {
			//console.log(arr[j][0]);
			//console.log(i);
			buck=getPosition(arr[ j ][0], i);
			//console.log(buck);
			//console.log(buckets[buck])
			if(buck!=NaN){
				buckets[getPosition(arr[ j ][0], i)].push(arr[ j ]); // pushing into buckets	
			}
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
	var alfCad=[];
	for(var i=0;i<cad.length;i++){
		alfCad.push(alfDict[cad.charAt(i)]);
	}
	alfCad.push(0);
	console.log(alfCad);
	
	
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
	
	var thriples=[];
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
	
	var thriplesArray=[];
	
	for(var i=0;i<thriples.length;i++){
		var thrip='';
		var currentT=thriples[i];
		for (var j=0;j<currentT[0].length;j++){
			thrip+=currentT[0][j].toString();
		}
		thriplesArray.push([parseInt(thrip),currentT[1]]);
	}
	
	//console.log(thriplesArray);
	
	var sortedThriples=radixSortTuple(thriplesArray);
	console.log("-----------sorted thriples-----------")
	console.log(sortedThriples);
	
	var tableRankThriple=[];
	var lastThr=[-1,-1];
	var currentRank=0;
	var duplicates=false;
	var b12IndexRank={};
	
	for(var i=0;i<sortedThriples.length;i++){
		currentTh=sortedThriples[i];
		console.log(currentTh[0])
		if(currentTh[0]!=lastThr[0]){
			currentRank+=1;
			tableRankThriple.push([currentTh,currentRank]);
			b12IndexRank[currentTh[1].toString()]=currentRank;
		}
		else{
			tableRankThriple.push([currentTh,currentRank]);
			b12IndexRank[currentTh[1].toString()]=currentRank;
			duplicates=true;
		}
		lastThr=currentTh;
	}
	console.log("----------------tableRankThriple----------------")
	console.log(tableRankThriple)
	
    b12IndexRank[cad.length.toString()]=0
    b12IndexRank[(cad.length+1).toString()]=0
    b12IndexRank[(cad.length+2).toString()]=0
	
	//console.log(tableRankThriple);
	
	var b0Tuples21=[];
	console.log(duplicates);
	if(duplicates){
		newArray=new Array(tableRankThriple.length+2);
		
		for(var i=0;i<b12.length+2;i++){
			var val=b12[i];
			if(val!=NaN && val!=undefined){
			newArray[i]=b12IndexRank[b12[i][1].toString()];;
			}
			else{
				newArray[i]=0;
			}
		}
		
		console.log(newArray);
		var str='';
		for(var i=0;i<newArray.length;i++){
			str+=newArray[i].toString();
		}
		
		var recReturn=dc3(str);
		console.log("--------recurse returned-------");
		console.log(recReturn);
		
		var sortedB12=new Array(b12.length);
		for(var i=1;i<recReturn.length;i++){
			b12Val=b12[recReturn[i]];
			sortedB12[i-1]=b12Val;
		}
		
		console.log("-------IndexRankOld-------")
		console.log(b12IndexRank);
		for(var i=0;i<sortedB12.length;i++){
			console.log(sortedB12[i][1].toString());
			b12IndexRank[sortedB12[i][1].toString()]=i+1;
		}
		console.log("-------updatedIndexRank------")
		console.log(b12IndexRank);
		
		
		console.log("--------b0-------");
		console.log(b0);
		
		for(var j=0;j<b0.length;j++){
			var intB=b12IndexRank[(b0[j][1]+1).toString()];
			var stringB=intB.toString();
			console.log([intB,(b0[j][1]+1).toString()]);
			console.log(j)
			b0Tuples21.push([parseInt(((b0[j][0]).toString())+stringB),[ [b0[j][0],intB],b0[j][1] ]]);
		}
		console.log("------b0unsorted------");
		console.log(b0Tuples21);
		b0Tuples21=radixSortTuple(b0Tuples21);
		console.log("------b0sorted------");
		console.log(b0Tuples21);
		
		var result=[];
		var idx=0;
		var idx2=0;
		
		while(idx<b0Tuples21.length && idx2<sortedB12.length){
			while(idx2<sortedB12.length && idx<b0Tuples21.length){
				//console.log("idx",idx)
				//console.log("idx2",idx2)
				var currentB0=b0Tuples21[idx];
				var idxB0=currentB0[1][1];
				var currentB12=sortedB12[idx2];
                var idxB12=currentB12[1];
				//console.log(idxB12);
				if(idxB12%3==2){
					var charB12=alfCad[idxB12];
                    var charB0=alfCad[idxB0];
					//console.log(charB12);
					//console.log(charB0);
                    if(charB0>charB12){
                        result.push(idxB12);
                        idx2=idx2+1;
					}
                    else if(charB0<charB12){
                        result.push(idxB0);
                        idx=idx+1;	
					}
                    else{
						var charB12P1=alfCad[idxB12+1];
                        var charB0P1=alfCad[idxB0+1];
                        if(charB0P1>charB12P1){
                            result.push(idxB12);
                            idx2=idx2+1	;
						}
                        else if(charB0P1<charB12P1){
                            result.push(idxB0);
                            idx=idx+1;
						}
                        else{
							var rankB0P2=b12IndexRank[(idxB0+2).toString()];
                            var rankB12P2=b12IndexRank[(idxB12+2).toString()];
							console.log(idxB0+2);
							console.log(idxB12+2);
                            if(rankB0P2>rankB12P2){
                                result.push(idxB12);
                                idx2=idx2+1;
							}
                            else if(rankB0P2<rankB12P2){
                                result.push(idxB0);
                                idx=idx+1;
							}
						}
					}   
				}
				else if(idxB12%3==1){
					var charB12=alfCad[idxB12];
                    var charB0=alfCad[idxB0];
                    if(charB0>charB12){
                        result.push(idxB12);
                        idx2=idx2+1;
					}
                    else if(charB0<charB12){
                        result.push(idxB0);
                        idx=idx+1;
					}
                    else{
						var rankB0P1=b12IndexRank[(idxB0+1).toString()];
                        var rankB12P1=b12IndexRank[(idxB12+1).toString()];
                        if(rankB0P1>rankB12P1){
                            result.push(idxB12);
                            idx2=idx2+1	;
						}
                        else if(rankB0P1<rankB12P1){
                            result.push(idxB0);
                            idx=idx+1;
						}
					}
				}
                    
			}
		}
		
		if(idx>=tableRankThriple.length && idx2!=b0Tuples21.length){
			for (var i=idx;i<b0Tuples21.length;i++){
				var currentB0=b0Tuples21[i];
                var idxB0=currentB0[1][1];
                result.push(idxB0);	
			}
		}
        else if(idx!=tableRankThriple.length && idx2>=b0Tuples21.length){
			for(var i=idx2;i<tableRankThriple.length;i++){
				var currentB12=tableRankThriple[i];
                var idxB12=currentB12[0][1];
                result.push(idxB12);
			}
		}
         return result;   
	}
	else{
		b0.pop()
		for(var i=0;i<b0.length;i++){
			var intB=b12IndexRank[(b0[i][1]+1).toString()];
			var stringB=intB.toString();
			b0Tuples21.push([parseInt((b0[i][0]).toString()+stringB),[[b0[i][0],intB],b0[i][1]]]);
		}
		b0Tuples21=radixSortTuple(b0Tuples21);
		console.log(b0Tuples21);
		var result=[]
        var idx=0
        var idx2=0
        while(idx<b0Tuples21.length && idx2<tableRankThriple.length){
			while(idx2<tableRankThriple.length && idx<b0Tuples21.length){
				var currentB0=b0Tuples21[idx];
                var idxB0=currentB0[1][1];
                var currentB12=tableRankThriple[idx2];
                var idxB12=currentB12[0][1];
                if(idxB12%3==2){
					var charB12=alfCad[idxB12];
                    var charB0=alfCad[idxB0];
                    if(charB0>charB12){
                        result.push(idxB12);
                        idx2=idx2+1;
					}
                    else if(charB0<charB12){
                        result.push(idxB0);
                        idx=idx+1;	
					}
                    else{
						var charB12P1=alfCad[idxB12+1];
                        var charB0P1=alfCad[idxB0+1];
                        if(charB0P1>charB12P1){
                            result.push(idxB12);
                            idx2=idx2+1;	
						}
                        else if(charB0P1<charB12P1){
                            result.push(idxB0)
                            idx=idx+1	
						}
                        else{
                            var rankB0P2=b12IndexRank[(idxB0+2).toString()];
                            var rankB12P2=b12IndexRank[(idxB12+2).toString()];
                            if(rankB0P2>rankB12P2){
                                result.push(idxB12);
                                idx2=idx2+1;
							}
                            else if(rankB0P2<rankB12P2){
                                result.push(idxB0);
                                idx=idx+1;
							}
						}
					}
				}
                    
                else if(idxB12%3==1){
					var currentB12=tableRankThriple[idx2];
                    var idxB12=currentB12[0][1];
                    var charB12=alfCad[idxB12];
                    var charB0=alfCad[idxB0];
                    if(charB0>charB12){
                        result.push(idxB12);
                        idx2=idx2+1;
					}
                    else if(charB0<charB12){
                        result.push(idxB0);
                        idx=idx+1;	
					}
                    else{
						var rankB0P1=b12IndexRank[(idxB0+1).toString()];
                        var rankB12P1=b12IndexRank[(idxB12+1).toString()];
                        if(rankB0P1>rankB12P1){
                            result.push(idxB12);
                            idx2=idx2+1;	
						}
                        else if(rankB0P1<rankB12P1){
                            result.push(idxB0);
                            idx=idx+1;	
						}
					}
				}
                    
			}
		}
		if(idx>=tableRankThriple.length && idx2!=b0Tuples21.length){
			for (var i=idx;i<b0Tuples21.length;i++){
				var currentB0=b0Tuples21[i];
                var idxB0=currentB0[1][1];
                result.push(idxB0);	
			}
		}
        else if(idx!=tableRankThriple.length && idx2>=b0Tuples21.length){
			for(var i=idx2;i<tableRankThriple.length;i++){
				var currentB12=tableRankThriple[i];
                var idxB12=currentB12[0][1];
                result.push(idxB12);
			}
		}
		console.log("---------result---------------")
		console.log(result)
         return result;  
	}
}

var cadena="yabbadabbado"

var res=dc3(cadena);
console.log(res);