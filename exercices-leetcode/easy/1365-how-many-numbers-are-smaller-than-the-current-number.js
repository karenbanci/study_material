/*
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {

  let count = 0;
  let arrayDeResultado = [];

  for (let i = 0; i < nums.length; i++){
    for (let j = 0; j < nums.length; j++){

      if( j != i && nums[j] < nums[i]){
        count++;
      }
    }
    arrayDeResultado.push(count);
    console.log("resultado:   " + arrayDeResultado)
    // nessa linha vou zerar a contagem para o loop do j fazer uma nova contagem
    count = 0;
  }

  return arrayDeResultado
};

const nums = [8, 1, 2, 2, 3];
// Output: [4,0,1,1,3]
console.log(smallerNumbersThanCurrent(nums));

/*
Runtime: 93 ms, faster than 86.20% of JavaScript online submissions for How Many Numbers Are Smaller Than the Current Number.

Memory Usage: 43.7 MB, less than 93.91% of JavaScript online submissions for How Many Numbers Are Smaller Than the Current Number. */
