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

export function radixSort(arr) {

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

