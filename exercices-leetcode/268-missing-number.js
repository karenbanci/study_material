/*
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
// var missingNumber = function (nums) {
//   const n = nums.length;

//   const sorted = nums.sort();
//   console.log("entrada ordenada: ", sorted);

//   // aqui eu vou deixar todos os valores achados falso pq nao foi comparado com a array de entrada ainda
//   const arrayDeAchados = Array(n + 1).fill(false);
//   // console.log("array principal", arrayDeAchados);

//   // iterar para cada elemento da array de entrada que está ordenada
//   for (let i = 0; i < sorted.length; i++) {
//     // ordenar para cada elemento da array padrão
//     for (let j = 0; j < arrayDeAchados.length; j++) {
//       console.log("valor da padrao -----------", arrayDeAchados[j]);

//       // se cada elemento da array de entrada corresponde a arrau padrão,  retornar o valor que está faltando
//       if (sorted[i] == j) {
//         arrayDeAchados[j] = true;

//   console.log("array padrao", arrayDeAchados);
//         // caso contrario, retorna console log OK
//       }
//     }
//   }
//   console.log("array padrao", arrayDeAchados);
//   // tenho um array em que todos os elementos sao true exceto um elemento que é falso, e preciso retornar o indice desse elemento falso
//   for(let i = 0; i < arrayDeAchados.length; i++) {
//     if(arrayDeAchados[i] == false){
//       console.log("numero que faltava: " + arrayDeAchados[i]);
//       return i;
//     }
//   }

// };

var missingNumber = function (nums) {
  const n = nums.length;
  let somaDeTodosOsValoresDaArray = (n * (n+1)) / 2;
  console.log("soma: " + somaDeTodosOsValoresDaArray);

  for (let i = 0; i < nums.length; i++){
    somaDeTodosOsValoresDaArray -= nums[i];
  }
  return somaDeTodosOsValoresDaArray;

}

const nums = [9, 6, 4, 2, 3, 5, 7, 0, 1];
console.log(missingNumber(nums));
