/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
*/
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  // fazer a iteração de cada elemento na string;
  let newArray = [];

  for(let i = 0; i < strs.length; i++) {
    let arrayDeComparacao = strs.shift();
    console.log('removido: ' + arrayDeComparacao)

  }






  return newArray
};

const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs));

const output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]];
console.log('saída esperada: ' + output);
