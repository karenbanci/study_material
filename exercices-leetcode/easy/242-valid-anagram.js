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

*/
/*
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
*/
/*
const a = "anagram";
const b = "nagaram";

split1 = ["a", "n", "a", "g", "r", "a", "m"];
split2 = ["n", "a", "g", "a", "r", "a", "m"];

hashmap1 = { "a":1 }
hashmap1 = { "a":1 , "n":1" }
hashmap1 = { "a":2 , "n":1" }
hashmap1 = { "a":2 , "n":1", "g":1 }
hashmap1 = { "a":2 , "n":1", "g":1, "r":1 }
hashmap1 = { "a":3 , "n":1", "g":1, "r":1 }
hashmap1 = { "a":3 , "n":1", "g":1, "r":1, "m":1 }

the same thing to hashmap2

in the end....
hashmap1 = { "a":3, "g":1, "m":1, "n":1, "r":1};
hashmap2 = { "a":3, "g":1, "m":1, "n":1, "r":1};

Comparte if hashmap1 == hashmap2 -> true
Comparte if hashmap1 !== hashmap2 -> false

*/

//Made with hash map
var isAnagram = function (s, t) {
  const hashmap1 = new Map();
  const hashmap2 = new Map();

  if (s.length !== t.length) return false;

  for (let c in s) {
    //para incrementar +1 no valor a cada chave que se repete
    // O operador de coalescência nula (??) é um operador lógico que retorna o seu operando do lado direito quando o seu operador do lado esquerdo é null ou undefined. Caso contrário, ele retorna o seu operando do lado esquerdo.
    // tem dois casos, 1) se a chave não existe ele pega o valor 0 e adiciona o valor 1; 2) se existe ele pega o valor dessa chave e adiciona 1.
    const value = (hashmap1.get(s[c]) ?? 0) + 1;
    const key = s[c];
    hashmap1.set(key, value);
  }
  // console.log("map S: ", hashmap1);

  for (let c in t) {
    //para incrementar +1 no valor a cada chave que se repete
    const value = (hashmap2.get(t[c]) ?? 0) + 1;
    const key = t[c];
    hashmap2.set(key, value);
  }
  // console.log("map T: ", hashmap2);

  // comparação por referência
  if (compareMaps(hashmap1, hashmap2)) {
    return true;
  } else {
    return false;
  }


};

function compareMaps(map1, map2) {
  var testVal;
  if (map1.size !== map2.size) {
    return false;
  }
  for (var [key, val] of map1) {
    testVal = map2.get(key);
    // in cases of an undefined value, make sure the key
    // actually exists on the object so there are no false positives
    if (testVal !== val || (testVal === undefined && !map2.has(key))) {
      return false;
    }
  }
  return true;
}

let time = new Date();
let msAntes = time.getMilliseconds();
const a = "anagram";
const b = "nagaram";
console.log("teste 1: " + isAnagram(a, b));

time = new Date();
let msDepois = time.getMilliseconds();
console.log("demorou: " +( msDepois - msAntes) + " ms");

console.log("--------------------");
const c = "rat";
const d = "car";
console.log("teste 2: " + isAnagram(c, d));


time = new Date();
let msDepois2 = time.getMilliseconds();
console.log("demorou: " + (msDepois2 - msDepois) + " ms");

console.log("--------------------");
const s = "caramelo";
const t = "chocolat";
console.log("teste 2: " + isAnagram(s, t));

time = new Date();
let msDepois3 = time.getMilliseconds();
console.log("demorou: " + (msDepois3 - msDepois2) + " ms");
