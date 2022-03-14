/*
tenho que pegar cada elemento da array e somar com o elemento seguinte


index.  0. 1. 2. 3
nums = [1, 2, 3, 4]

sum[0]    index 0             = 1
sum[1]    index 0 + index 1   = 3
sum[2]    index 1 + index 2   = 6
sum[3]    index 2 + index 3   = 10

ou seja

for (let i = 0; i < nums.length; i++){
    let sum = nums[i]+nums[i]
}
return sum
*/
var runningSum = function (nums) {
  // aqui eu deixei i=1 pq nao quero que o index 0 mude seu valor, quero que permaneça o mesmo
  for (let i = 1; i < nums.length; i++) {
  // aqui eu pego index atual nums[i] e somo com o valor do index anterior nums[i-1]
    nums[i] = nums[i] + nums[i - 1];
  }
  return nums;
};
