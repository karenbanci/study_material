/*
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
*/
/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
  // usarei essa array para armazenar o resultado no final
  let result = [];

  // var max = Math.max(...arr);

  // aqui estou usando o reduce que vai retornar o maior valor dentre a array
  const maxValue = candies.reduce(function (prev, current) {
    // se prev for maior que atual, retorna prev, caso contrário retorna curr.
    return prev > current ? prev : current;
  });

  console.log(maxValue);

  for (let i = 0; i < candies.length; i++) {
    const recebeuDoceExtra = candies[i] + extraCandies;

    if (recebeuDoceExtra >= maxValue) {
      console.log(
        "O valor: " + recebeuDoceExtra + " é maior ou igual a: " + maxValue
      );
      result.push(true);
    } else {
      result.push(false);
    }
  }
  // kidsWithCandies(candies, extraCandies);
  return result;
};

const candies = [2, 3, 5, 1, 3];
const extraCandies = 3;
console.log(kidsWithCandies(candies, extraCandies))

 /*
 Runtime: 73 ms, faster than 85.28% of JavaScript online submissions for Kids With the Greatest Number of Candies.

Memory Usage: 42 MB, less than 94.39% of JavaScript online submissions for Kids With the Greatest Number of Candies. */
