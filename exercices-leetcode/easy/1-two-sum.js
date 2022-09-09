/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

    ------- iterar cada elemento de nums
    index   0 1 2 3 4
    nums = [2,7,11,15]

    index 0 + index 1 === target? se sim retorna [nums[i], nums[j]]
*/

// nums[i] + nums[j] = target
// return [nums[i], nums[j]]

var twoSum = function (nums, target) {

  for (let i = 0; i < nums.length; i++) {
    // console.log('index i:', nums[i]);

    for (let j = i+1; j < nums.length; j++) {
    // console.log("index j:", nums[j]);

      if(nums[i] + nums[j] === target) {
        console.log("o numero é : ", nums[i], nums[j])
        console.log("nums[i]:", [i])
        console.log("nums[j]:", [j]);

        return [i,j];
      }
    }
  }
};

const nums = [2,5,5,11];
const target = 10;

console.log(twoSum(nums, target))
