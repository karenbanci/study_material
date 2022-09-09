/*
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
*/
/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
const createTargetArray = (nums, index) => {
  let target = [];

  // para cada index de nums, adiciona dentro do target no index[i] que for destinado
  for (const i in nums) target.splice(index[i], 0, nums[i]);
  return target;
};

const nums = [0, 1, 2, 3, 4];
const index = [0, 1, 2, 2, 1];

console.log(createTargetArray(nums, index));

/*
Runtime: 59 ms, faster than 96.60% of JavaScript online submissions for Create Target Array in the Given Order.

Memory Usage: 41.7 MB, less than 93.06% of JavaScript online submissions for Create Target Array in the Given Order. */
