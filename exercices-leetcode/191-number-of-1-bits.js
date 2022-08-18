/*
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
The input must be a binary string of length 32.
*/

var hammingWeight = function (n) {
  let count = 0;
  const number = n.toString(2).split('');
  console.log(number);

  for (let i = 0; i < number.length; i++) {
    if(number[i] > 0){
      count++;
    }
  }
  return count
};

const a = 0b0000000000000000000000010000000;
console.log('esperado: 1');
console.log('caso A resultado', hammingWeight(a));
console.log("----------------------------------------");


const b = 0b0000000000000000000000000001011;
console.log("esperado: 3");
console.log("caso B resultado", hammingWeight(b));
console.log("----------------------------------------");

const c = 0b11111111111111111111111111111101;
console.log("esperado: 31");
console.log("caso C resultado", hammingWeight(c));


let d = 0b1000;
let e = 0b0110;
console.log('resultado do calculo d ', d-e);

console.log("resultado do calculo b ", (d - e).toString(2));
