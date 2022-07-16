/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

* @param {string} s
* @param {string}
* @return {boolean}

1. verificar o tamanho dessas duas arrays, se tiverem o mesmo tamanho continue

2. separar cada caracter

*/

var isAnagram = function(s, t) {
  console.log("string s:", s);
  console.log('string t:', t);

  if(s.length === t.length){
    const string1 = s.split('').sort().join('');
    console.log("string 1:", string1);

    const string2 = t.split("").sort().join("");
    console.log("string 2:", string2);

    if(string1 === string2){
      console.log("é um anagrama")
      return true;
    } else {
      console.log("sao diferentes");
      return false;
    }

  }
  return false;
};

// const s = "anagram";
// const t = "nagaram";

// const s = "rat";
// const t = "car";

const s = "caramelo";
const t = "chocolat";

console.log(isAnagram(s, t));
