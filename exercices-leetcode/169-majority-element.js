/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
*/

var majorityElement = function (nums) {
  let n = nums.length;
  let metade = n / 2;

  const objeto = new Object();

  for (let i = 0; i < n; i++) {
  // criar elementos em um objeto
    if(objeto[nums[i]]){
      objeto[nums[i]]++;
    } else {
      objeto[nums[i]] = 1;
    }

  }
  console.log(objeto);
  let keys = Object.keys(objeto);

  for (let j = 0; j < keys.length; j++) {
    if(objeto[keys[j]] >= metade){
      return keys[j]
    }
    console.log(objeto);
  }


};

const nums = [8, 8, 7, 7, 7];

console.log(majorityElement(nums));
