/*
primeiro passo, pegar a array e dividir no meio
primeira metade vai ser X e segunda metade vai ser Y

depois vou ter que juntar as duas arrays em X1,Y1,X2,Y2,X3,Y3

nums = [1,2,3,1,2,3]
n = nums.length / 2 // 3

para i = nums          i = 0; i < n ; i++

            i
index   0       1       2
nums    1       2       3

            j
index   3       4       5
n       1       2       3

pegar
nums[0], nums[3], nums[1], nums[4], nums[2], nums[5]
    [i],  [i+n]    [i]   [i+n]    [i]    [i+n]

*/

var shuffle = function (nums, n) {
  let result = [];
  for (let i = 0; i < n; i++) {
    result.push(nums[i], nums[i + n]);
  }
  // console.log(result)
  return result;
};
