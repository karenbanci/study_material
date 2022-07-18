/* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.*/

/* Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] */


// Ex: 1  - esperado: [0,1]
// const nums = [2,7,11,15];
// let target = 9;

// Ex: 2 - esperado: [2,4]
// let nums = [-1, -2, -3, -4, -5];
// let target = - 8;

// Ex: 3 - esperado: [0,2]
// const nums = [-3, 4, 3, 90];
// let target = 0;

// Ex: 4  - esperado: [0,1]
// const nums = [3,3];
// let target = 6;


// funcao que irá fazer busca binária
const sumNum = function (nums, target) {
  // index do primeiro item da array
  let firstIndex = 0;
  // index do último item da array
  let lastIndex = nums.length - 1;
  // Guardamos o nums original para uso futuro
  let numsOriginal = nums.slice();

  // nums é ordenado numericamente
  nums = nums.sort(function (a, b) {
    return a - b;
  });


  // enquanto for verdadeiro, ele vai rodar e buscar a media do index da array
  while (true) {
    // soma dos valores do index
    let sum = nums[firstIndex] + nums[lastIndex];
    // console.log('Soma: ' + sum);

    // vai buscar a média do index da array e arredondar.
    // console.log(firstIndex, lastIndex);

    // aqui estou comparando se a soma é igual o alvo
    if (sum === target){
      // console.log('Valores : ', nums[firstIndex], nums[lastIndex]);
      // se for igual, ele retorna uma array com os index
      let firstOriginalIndex = numsOriginal.indexOf(nums[firstIndex]);
      // Destruimos o numero, para que o do last index nao seja repetido
      numsOriginal[firstOriginalIndex] = Math.NaN;
      return [firstOriginalIndex, numsOriginal.indexOf(nums[lastIndex])].sort(
        function (a, b) {
          return a - b;
        }
      );
    }

    // aqui estou comparando se o target é menor que o último index
    // se for, ele vai voltar um index pra baixo
    if (target < sum){
      lastIndex--;
      // console.log("procure de novo --");
      // aqui estou comparando se o target é maior que o primeiro index
      // se for, ele vai andar um index pra cima
    } else { //if (target > sum){
      firstIndex++;
      // console.log('procure de novo ++')
    }
  }

// fecha a função
}

console.log(sumNum(nums,target));
