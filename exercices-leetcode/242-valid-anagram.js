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
* @param {string} t
* @return {boolean}

*/

var isAnagram = function(s, t) {
  console.log(s,t)
  if(s.length === t.length){
    const arr1 = s.split('');
    const arr1Sorted = arr1.sort();
    console.log(arr1Sorted);

    const arr2 = t.split('');
    const arr2Sorted = arr2.sort();
    console.log(arr2Sorted);


    if(_.isEqual(arr1Sorted, arr2Sorted)){
      return true;
    } else {
      false
    }



  }
};

// const s = "anagram";
// const t = "nagaram";

const s = "rat";
const t = "car";

console.log(isAnagram(s, t));
