/*
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
Example 2:

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]*/

var buildArray = function(nums) {
  ans = [];
  for ( let i = 0; i < nums.length; i++){
      ans[i] = nums[nums[i]];
  }
  return ans
};

//  a array esta na ordem [0,2,1,5,3,4]

// a permutação foi reorganizar a array para que ela imprima o seguinte valor
//  organizar para que fique [0,1,2,4,5,3]

//  1 <= tamanho da array <= 1000
//  0 <= index da array < tamanho da array

// ans[i] = nums[nums[i]] ela pega o index da array nums 2x
// para cada valor da array 0 <= i < nums.length

/* ex 3
nums = [0,3,1,2]
ans[i] = nums[nums[i]]

ans[0] = nums[nums[0]] = nums[0] = 0

ans[1] = nums[nums[1]] = nums[3] = 2

ans[2] = nums[nums[2]] = nums[1] = 3

ans[3] = nums[nums[3]] = nums[2] = 1

ans = [0,2,3,1]
*/
