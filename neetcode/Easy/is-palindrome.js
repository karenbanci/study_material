/**
 * Is Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
*/

class Solution {
  /**
   * @param {string} s
   * @return {boolean}
   */
  isPalindrome(s) {
    let l = 0;
    let r = s.length - 1;

    while (l < r) {
      while (l < r && !this.alphaNum(s[l])) {
        l++;
      }
      while (r > l && !this.alphaNum(s[r])) {
        r--;
      }
      if (s[l].toLowerCase() !== s[r].toLowerCase()) {
        return false;
      }
      l++;
      r--;
    }
    return true;
  }

  alphaNum(c) {
    const charCode = c.charCodeAt(0);
    return (
      (65 <= charCode && charCode <= 90) ||
      (97 <= charCode && charCode <= 122) ||
      (48 <= charCode && charCode <= 57)
    );
  }
}

//chamar o class Solution
const solution = new Solution();
// console.log(solution.isPalindrome("Was it a car or a cat I saw?")); //true
console.log(solution.isPalindrome("tab a cat")); //false

// class Solution {
//   /**
//    * @param {string} s
//    * @return {boolean}
//    */
//   isPalindrome(s) {
//     const arr = s.split("");
//     const filteredArray = arr.filter((char) => /[a-zA-Z]/.test(char));
//     console.log("filteredArray", filteredArray);

//     const reversedArr = filteredArray.reverse();
//     console.log("reverseArr", reversedArr);

//     const str = filteredArray.join("");
//     console.log("string original", str);

//     const reversedStr = reversedArr.join("");
//     console.log("string revertida", reversedStr);

//     if (str === reversedStr) {
//       return true;
//     }
//     return false;
//   }
// }
