/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Example 4:
Input: nums = [14, 2, 24, 22, 22]
Output: true
*/

// for (let i = 0; i < nums.length; i++){
//   for (let j = nums[i+1]; j < nums.length; j++){
//     if (nums[i] === nums[j]){
//       return true;
//     } else {
//       return false
//     }
//   }
// }

var containsDuplicate = function (nums) {
  const setNums = new Set();

  for(const i of nums){
    if(setNums.has(i)){
      return true
    }
    setNums.add(i);
  }
  return false;
};

nums = [1,2,3,4];

console.log(containsDuplicate(nums));
