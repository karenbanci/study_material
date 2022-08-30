/*
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]

index:   01234567
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

*/

    /*
    indices[0] - result[4] = caracters[0] - C
    indices[1] - result[5] = caracters[1] - O
    indices[2] - result[6] = caracters[2] - D
    indices[3] - result[7] = caracters[3] - E
    indices[4] - result[0] = caracters[4] - L
    indices[5] - result[2] = caracters[5] - E
    indices[6] - result[1] = caracters[6] - E
    indices[7] - result[3] = caracters[7] - T

    só que automaticamente o result irá ordernar o index
    */

/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {

  const characters = s.split("");
  // console.log("caracteres separados: " + characters);
  let result = []

  for (const i in characters) {
    // aqui estou atribuindo o index do resultado para que seja igual ao index do caracters
    result[indices[i]] = characters[i];


    console.log("arrumado: " + result);
  }
  return result.join('')
};

// index   01234567
const s = "codeleet";
const indices = [4, 5, 6, 7, 0, 2, 1, 3];
console.log(restoreString(s, indices));

/*
Runtime: 113 ms, faster than 33.91% of JavaScript online submissions for Shuffle String.
Memory Usage: 43.9 MB, less than 97.01% of JavaScript online submissions for Shuffle String.
*/
