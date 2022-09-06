/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 105

*/

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
  const ans = [];
  // passo 1 - estou dissociando o valor N em uma array de n+1
  for(let i = 0; i < n+1; i++) {
    ans.push(i);
    console.log("dissociando o numero " + ans);
  }

  // passo 2 - transformando os números em binários
  for(let i = 0; i < ans.length; i++) {
    ans[i] = ans[i].toString(2);
    console.log("ans: " + ans);
  }

  //passo 3 - somar os caracteres dentro da string (numeros que começam com 1)
  let ans2 = [];
  for(let i = 0; i < ans.length; i++) {
    // aqui vou armazenar a soma dos caracteres dentro da string, o valor começa com 0
    let somaDosCaracteres = 0;
    for (let j = 0; j < ans[i].length; j++) {
      // aqui estou acessando cada caractere dentro de cada index
      let caractere = ans[i].charAt(j);
      // se o valor do caractere for diferente de zero
      if (caractere != 0) {
        // soma os valores dos caracteres
        somaDosCaracteres++;
      }
    }
    console.log("resultado R:" + somaDosCaracteres);
    ans2.push(somaDosCaracteres);
  }
  return ans2;
};

// var countBits = function (num) {
//   let bits = [];
//   for (let i = 0; i <= num; i++)
//     // remove 0 from bits
//     bits.push(Number(i).toString(2).replace(/0/g, "").length);
//   return bits;
// };
console.log(countBits(2))
