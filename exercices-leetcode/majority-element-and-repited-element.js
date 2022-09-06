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
  const objeto = new Object();
  let metade = nums.length / 2;

  for (let num in nums) {
    if (objeto[nums[num]]) {
      objeto[nums[num]]++;
    } else {
      objeto[nums[num]] = 1;
    }
  }
  console.log("objeto: " + JSON.stringify(objeto));

  let result = Object.keys(objeto);

  for (let key in result) {
    if (objeto[result[key]] >= metade) {
      return result[key];
    }
  }
};

const nums = [2, 2, 2, 4, 4, 4, 4, 8,  4];

console.log(majorityElement(nums));

console.log("---------------------------------------");

//  este problema retorna os caracteres repetidos dentro de uma string, ele leva em consideração espaço
var repeatedElement = function (string) {
  const separado = string.split("");
  console.log('separado: ' + separado);

  const objeto = new Object();

  // let metade = separado.length / 2;

  for (let c in separado) {
    if (objeto[separado[c]]) {
      objeto[separado[c]]++;
    } else {
      objeto[separado[c]] = 1;
    }
  }
  console.log("objeto: " + JSON.stringify(objeto));

  let result = Object.keys(objeto);
  let retornarResultado = [];

  for (let key in result) {
    if (objeto[result[key]] >= 2) {
      retornarResultado.push(result[key]);
    }
  }
  return retornarResultado;
};
const string = "letra repetida";

console.log(repeatedElement(string));
