/*
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.



Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
*/



/* primeiro identificar os index de cada elemento da array,

a array ans é formada

ans[i] == nums[i]

vou ter que fazer um push para adicionar os elementos na array ans


index.  0  1. 2. 3
nums = [1, 2, 3, 4]

index. 0  1. 2. 3. 4. 5. 6. 7
ans = [1, 2, 3, 4, 1, 2, 3, 4]

Vou ter que pegar a array de tamanho n e depois duplicar a array e fica no final 2n

pegar o index 0 e copiar o valor dele e adicionar no final da array
repetir para cada index

to pegando cada elemento index da array
array nums
for (let i = 0; i < nums.length; i++) {

quando eu peguei o index 0, vou copiar o valor dele e adicionar no final
quando eu peguei o index 1, vou copiar o valor dele e adicionar no final

os elementos terao que ser add

let ans = nums.concat(nums)

   index    index
ans[0] = nums[0]
ans[1] = nums[1]
ans[2] = nums[2]
ans[3] = nums[3]
ans[4] = nums[0]
ans[5] = nums[1]
ans[6] = nums[2]
ans[7] = nums[3]

}
*/


var getConcatenation = function (nums) {
  let ans = nums.concat(nums);
  return ans;

  //OU dessa maneira abaixo
  //     let ans=[]
  //     for (let i = 0; i < nums.length; i++) {
  //         ans.push(nums[i])
  //     }
  //     for (let i = 0; i < nums.length; i++) {
  //         ans.push(nums[i])
  //     }

};
