/**
 * Foreign Dictionary
Solved
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
 *
 */

class Solution {
  /**
   * @param {string[]} words
   * @returns {string}
   */

  foreignDictionary(words) {
    let beforeChar = new Map();
    let afterChar = new Map();

    let charSet = new Set();

    for (let word of words) {
      // console.log("word", word)
      for (let letter of word) {
        // console.log("letter", letter)
        charSet.add(letter);
      }
    }

    for (let char of charSet) {
      beforeChar.set(char, new Set());
      afterChar.set(char, new Set());
    }

    for (let i = 0; i < words.length - 1; i++) {
      console.log("test", words[i], words[i + 1]);
      let word1 = words[i];
      let word2 = words[i + 1];
      let firstDiffCharIndex = 0;

      //
      while (
        firstDiffCharIndex < word1.length &&
        firstDiffCharIndex < word2.length &&
        word1[firstDiffCharIndex] == word2[firstDiffCharIndex]
      ) {
        firstDiffCharIndex++;
      }
      if (
        firstDiffCharIndex < word1.length &&
        firstDiffCharIndex < word2.length
      ) {
        let firstBeforeChar = word1[firstDiffCharIndex];
        let firstAfterChar = word2[firstDiffCharIndex];

        beforeChar.get(firstBeforeChar).add(firstAfterChar);
        afterChar.get(firstAfterChar).add(firstBeforeChar);
      } else if (
        firstDiffCharIndex < word1.length &&
        firstDiffCharIndex == word2.length
      ) {
        return "";
      }
    }
    let queue = [];

    for (let [key, val] of afterChar) {
      if (val.size === 0) {
        queue.push(key);
      }
    }
    console.log("after", afterChar, "before", beforeChar);
    let aphabetic = "";

    while (queue.length !== 0) {
      let currentChar = queue.pop();
      aphabetic += currentChar;

      // add more chars to process
      console.log(beforeChar.get(currentChar));
      // beforeChar.get(currentChar).forEach (function(afterCurrChar) {
      //     afterChar.get(afterCurrChar).delete(currentChar)
      //     if( afterChar.get(afterCurrChar).size === 0) {
      //         queue.push(afterChar)
      //     }
      // })
      for (let afterCurrChar of beforeChar.get(currentChar)) {
        console.log(afterCurrChar);
        afterChar.get(afterCurrChar).delete(currentChar);
        if (afterChar.get(afterCurrChar).size === 0) {
          queue.push(afterCurrChar);
        }
        // console.log("line 64", afterChar)
      }
    }

    console.log("aphabetic", aphabetic);

    if (aphabetic.length === charSet.size) {
      return aphabetic;
    }
    return "";
  }
}
