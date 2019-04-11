/*
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the
maximum values of each subarray of length k."
 */

//O(Nk) time
function computeMaxPerSubarray(array, k) {
    let buffer = array.slice(0, k-1);
    for (let i = k-1; i < array.length; i++ ) {
        buffer.push(array[i]);
        console.log(buffer);
        console.log(Math.max(...buffer));
        buffer.shift();

    }
}

function computeMaxFaster(array, k){

}


computeMaxPerSubarray( [10, 5, 2, 7, 8, 7], 3);
console.log("faster")
computeMaxFaster( [10, 5, 2, 7, 8, 7], 3);