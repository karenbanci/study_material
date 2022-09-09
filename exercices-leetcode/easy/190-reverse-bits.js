/*
Reverse bits of a given 32 bits unsigned integer.


Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)

Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
*/
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */

var reverseBits = function(n) {

  console.log('decimal: ', n);

  // convertendo em string, separando cada item, reverter e juntar
  // padStart tenho que informar o tamanho da minha string e ele vai completar com '0'.
  const binaryToString = n.toString(2).padStart(32, '0').split("").reverse().join("");
  console.log('binary: ', binaryToString)

  //converter em decimal
  let result = parseInt(binaryToString, 2);

  console.log('resultado: ', result)
  return result;

};

const n = 0b00000010100101000001111010011100; // 43261596
// return = 00111001011110000010100101000000 // 964176192
console.log(reverseBits(n));
