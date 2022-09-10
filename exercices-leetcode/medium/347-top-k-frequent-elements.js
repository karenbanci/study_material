/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const map = new Map();
  let array = [];
  let bucket = Array.from({ length: nums.length + 1 }, () => []);

  for (let i = 0; i < nums.length; i++) {
    //estou assignando o valor da chave, para cada index da chave  somar 1 se tiver o valor, se não, mantenha 1
    map[nums[i]] = nums[i] in map ? 1 + map[nums[i]] : 1;
  }
  console.log("completando: " + JSON.stringify(map));

  //aqui estou colocando 
  for (const c in map) {
    bucket[map[c]].push(c);
  }

  for (let j = bucket.length - 1; j >= 0; j--) {
    if (bucket[j].length > 0) {
      bucket[j].forEach((elem) => array.push(elem));
      if (k == array.length) {
        return array;
      }
    }
  }

  return array;
};

//Output: [1,2]
const nums = [1, 1, 1, 2, 2, 3];
const k = 2;
console.log(topKFrequent(nums, k));

console.log("-------------------------");
const meuMapDeTeste = new Map();
meuMapDeTeste.set(2, 4);

console.log("resultado:   " + JSON.stringify(meuMapDeTeste.get(2)));
