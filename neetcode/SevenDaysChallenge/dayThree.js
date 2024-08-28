/**
 * O problema consiste em debugar um código existente para transformá-lo em uma função que organize uma lista de números inteiros distintos em uma "sequência zig-zag".

Uma sequência é considerada uma sequência zig-zag se os primeiros `k` elementos da sequência estiverem em ordem crescente e os últimos `k` elementos estiverem em ordem decrescente, onde `k = (n + 1) / 2`, e `n` é o número de elementos na lista.

O objetivo é encontrar a menor sequência zig-zag possível em ordem lexicográfica (ou seja, a primeira em ordem alfabética se considerarmos as sequências como palavras).

### Exemplo:

Dada a lista `[2, 3, 5, 1, 4]`, a função deve reorganizar os elementos para obter a sequência zig-zag `[1, 2, 5, 4, 3]`.

 */

// function processData(input) {
//   input = input.sort((a, b) => a - b);
//   console.log(input);

//   const mid = parseInt((input.length - 1) / 2);
//   let temp = input[mid];
//   input[mid] = input[input.length - 1];
//   input[input.length - 1] = temp;
//   console.log(input);

//   let start = mid + 1;
//   let end = input.length - 2;

//   while (start <= end) {
//     let temp = input[start];
//     input[start] = input[end];
//     input[end] = temp;

//     start++;
//     end--;
//   }

//   console.log(input);
//   return input;
// }

// // processData([2,3,5,1,4])
// processData([1, 2, 3, 4, 5, 6, 7]);

/**
 * Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
 */

// function caesarCipher(s, k) {
//   let alfabeto = "abcdefghijklmnopqrstuvwxyz";
//   let sArray = s.split("");

//   for (let i = 0; i < sArray.length; i++) {
//     let currentLetter = sArray[i];
//     let isUpperCase = currentLetter === currentLetter.toUpperCase();

//     // Converte a letra para minúscula para encontrar o índice
//     let letterIndex = alfabeto.indexOf(currentLetter.toLowerCase());

//     console.log("letter Index", letterIndex);

//     if (letterIndex !== -1) {
//       // A letra existe no alfabeto
//       let newIndex = (letterIndex + k) % alfabeto.length;
//       let newLetter = alfabeto[newIndex];

//       // Se a letra original era maiúscula, converte de volta para maiúscula
//       sArray[i] = isUpperCase ? newLetter.toUpperCase() : newLetter;
//     } else {
//       sArray[i] = currentLetter;
//     }
//   }

//   console.log(sArray.join(""));
//   return sArray.join("");
// }

// // caesarCipher("love", 3)
// caesarCipher("middle-Outz", 2);

// function palindromeIndex(s) {
//   let newArr = s.split("");
//   let indexRight;
//   console.log(newArr);

//   for (let indexLeft = 0; indexLeft < newArr.length; indexLeft++) {
//     indexRight = newArr.length - indexLeft - 1;
//     console.log("Left", newArr[indexLeft], "Right", newArr[indexRight]);
//     console.log("indexLeft", indexLeft, "indexRight", indexRight);

//     while (indexLeft <= indexRight) {
//       // console.log("impressao")
//       if (newArr[indexLeft] !== newArr[indexRight]) {
//         newArr.pop(newArr[indexRight]);
//         console.log("diferentes");
//         return indexRight;
//       }
//       console.log("iguais");
//       break;
//     }
//   }
//   return -1;
//   console.log("palindromo");
//   console.log(newArr);
// }

// palindromeIndex("aaab");
// palindromeIndex("cac");
