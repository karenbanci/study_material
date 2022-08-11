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
  // metade is a half of array
  //half means that if the number repeats more than half of times, example: If array size is 5, the number has to repeat more than 3 times (2.5 rounds to 3)
  let metade = n / 2;

  // new object, is empty
  const objeto = new Object();

  for (let i = 0; i < n; i++) {
    // encrease value into the object, how many numbers are repeated
    if (objeto[nums[i]]) {
      // if exist this key, encrease +1
      objeto[nums[i]]++;
      // else, keep the value 1
    } else {
      objeto[nums[i]] = 1;
    }
  }
  console.log(objeto);
  // here, I will check
  let keys = Object.keys(objeto);

  // check each key
  for (let j = 0; j < keys.length; j++) {
    // if the number of numbers is greater than half of the array
    if (objeto[keys[j]] >= metade) {
      // return key
      return keys[j];
    }
    console.log(objeto);
  }
};

const nums = [8, 8, 7, 7, 7];

console.log(majorityElement(nums));
