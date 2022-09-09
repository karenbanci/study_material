/*
There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.

Example 1:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]≈
*/

/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {

  return encoded.reduce((prev, curr, i)=> {
    // pegando o encoded[0] fazer push (enconded[0] ^ enconded[1]) e assim em diante

    prev.push(prev[i] ^ curr);
    console.log(prev);
    return prev;
    /*
    index     0 1 2
    enconded [1,2,3]
        ------ começou do 1 pq é o first
      index     0
    enconded = [1]
    então ... enconded.push(1 ^ 1) = 0
    enconded = [1 , 0]
    então ... enconded.push(1 ^ 2) = 2
    enconded = [1 , 0 , 2]
    então ... enconded.push(2 ^ 3) = 1
    enconded = [1 , 0 , 2, 1]
    */


    // estou começando a partir do index 0
  }, [first])
};

const encoded = [1, 2, 3];
const first = 1;

console.log(decode(encoded, first));

/*

Runtime: 137 ms, faster than 57.89% of JavaScript online submissions for Decode XORed Array.

Memory Usage: 48.4 MB, less than 86.84% of JavaScript online submissions for Decode XORed Array.*/
