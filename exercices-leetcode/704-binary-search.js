/*
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
*/

var search = function (nums, target) {
  // find index retorna -1 automaticamente se nao encontrar target
  const index = nums.findIndex(nums => nums === target);

  return index
};

const n = [-1, 0, 3, 5, 9, 12];
const t = 2;

console.log(search(n, t))
