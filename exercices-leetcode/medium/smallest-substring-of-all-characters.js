/*
Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"

Constraints:
[time limit] 5000ms
[input] array.character arr
1 ≤ arr.length ≤ 30
[input] string str
1 ≤ str.length ≤ 500
[output] string
*/

function getShortestUniqueSubstring(arr, str) {
  // separando os caracteres de entrada
  const elements = str.split("");
  // console.log("string separada: " + elements);

  let newString = "";


  // aqui será determinada a quantidade de pares que farão a varredura na string
  const quantityOfCaractereToSweep = arr.length;
  // console.log(
  //   "quantidade de elementos para varredura: " + quantityOfCaractereToSweep
  // );

  for (let j = quantityOfCaractereToSweep; j <= elements.length; j++) {
    // fazendo iteração para cada elemento da string
    for (let i = 0; i < elements.length; i++) {
      // console.log("i: " + i);
      // console.log("j: " + j);


      //aqui será a cópia da array (substring temporária)
      let sliced = elements.slice(i, i + j);
      // console.log("slicedado: " + sliced);

      // cópia da array inicial
      const comparador = arr.slice();

      // aqui comparando se o resultado com os caracteres invertidos ou caracteres normal for igual a array de entrada, colocar dentro da string vazia

      for(let k = 0 ; k < sliced.length; k++){
        //criando uma variável para pegar o elemento do comparador
        const indiceDoElementoK = comparador.indexOf(sliced[k]);
        // se o elemento k estiver no comparador
        if (indiceDoElementoK !== -1) {
          //remover o elemento k de dentro do comparador
          comparador.splice(indiceDoElementoK, 1);
        }
      }
      //se o comparador estiver vazio
      if (!comparador.length) {

        return sliced.join("");
      }
    }
  }

  return newString;
}

const arr = ["x", "y", "z"];
const str = "xyyzyzxy";
console.log("retorna: " + getShortestUniqueSubstring(arr, str));
console.log("esperado: yzx");

console.log("-----------------------------");
const entrada1 = ["x", "y", "z"];
const entrada2 = "xyyzyzyx";
console.log("retorna: " + getShortestUniqueSubstring(entrada1, entrada2));
console.log("esperado: zyx");

console.log("-----------------------------");
const entrada13 = ["x", "y", "z"];
const entrada23 = "xyxxz";
console.log("retorna: " + getShortestUniqueSubstring(entrada13, entrada23));
console.log("esperado: yxxz");

console.log("-----------------------------");
const entrada14 = ["x", "y", "z"];
const entrada24 = "xyyyyyyz";
console.log("retorna: " + getShortestUniqueSubstring(entrada14, entrada24));
console.log("esperado: xyyyyyyz");
