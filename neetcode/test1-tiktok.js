/* "use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}


 * Complete the 'GetOptimalContentStorage' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY tiktokStorage as parameter.


// first case
// index    0.  1. 2  3  4.      0  1  2. 3. 4
//          [1, 0, 1, 0, 1]  -> [0, 0, 1, 1, 1] - 1 operation
// swap arr[0] and arr[3]

// second case
//index     0   1  2  3  4. 5  6. 7. 8       0. 1. 2. 3. 4. 5. 6. 7. 8
//          [1, 0, 0, 1, 1, 0, 0, 0, 1]    [1, 1, 0, 1, 1, 0, 0, 0, 0]
// fist operation   arr[1]  and arr[8]

//.   0. 1. 2. 3. 4. 5. 6. 7. 8      0. 1. 2. 3. 4. 5. 6. 7. 8
//   [1, 1, 0, 1, 1, 0, 0, 0, 0] -> [1, 1, 1, 1, 0, 0, 0, 0, 0]
// second operation   arr[2]  and arr[4]
*/

// const { right } = require("inquirer/lib/utils/readline");

// complexidade da função interira -> O(nˆ2)
// function GetOptimalContentStorage(tiktokStorage) {
//   console.log("tiktokStorage::::::::::::", tiktokStorage);
//   // Write your code here
//   let operations = 0;
//   let temp = 0;

//   let empilhar_para = "";
//   let counter_left = 0;
//   let counter_right = 0;
//   // determinar a direção do algorítmo
//   for (let left = 0; left < tiktokStorage.length; left++) {
//     // O(n) - tempo
//     let right = tiktokStorage.length - left - 1;
//     console.log("left", left, "right", right);
//     if (left >= right) {
//       console.log("parar");
//       if (counter_left > counter_right) {
//         empilhar_para = "esquerda";
//       } else {
//         empilhar_para = "direita";
//       }
//       break;
//     }
//     if (tiktokStorage[left] === 1) {
//       counter_left++;
//     }
//     if (tiktokStorage[right] === 1) {
//       counter_right++;
//     }
//   }
//   console.log("empilhar_para ---->", empilhar_para);
//   console.log("counter_left", counter_left);
//   console.log("counter_right", counter_right);

//   // seria um jeito para otimizar a complexidade de tempo de O(n^2) para O(n)
//   // while (left < right && operations < maxOperations) {
//   //   if (tiktokStorage[left] === 0 && tiktokStorage[right] === 1) {
//   //     // Swap elements
//   //     let temp = tiktokStorage[left];
//   //     tiktokStorage[left] = tiktokStorage[right];
//   //     tiktokStorage[right] = temp;
//   //     operations++;
//   //     left++;
//   //     right--;
//   //  }}

//   for (let left = 0; left < tiktokStorage.length; left++) {
//     // O(nˆ2/2) -> O(nˆ2) - tempo
//     for (let right = tiktokStorage.length - 1; right > left; right--) {
//       if (left > right) {
//         break;
//       }

//       console.log("tiktokStorage::::::::::::", tiktokStorage);

//       if (empilhar_para === "direita") {
//         if (tiktokStorage[left] === 1 && tiktokStorage[right] === 0) {
//           temp = tiktokStorage[left];
//           tiktokStorage[left] = tiktokStorage[right];
//           tiktokStorage[right] = temp;
//           operations++;
//         } else {
//         }
//       } else if (empilhar_para === "esquerda") {
//         if (tiktokStorage[left] === 0 && tiktokStorage[right] === 1) {
//           temp = tiktokStorage[left];
//           tiktokStorage[left] = tiktokStorage[right];
//           tiktokStorage[right] = temp;
//           operations++;
//         } else {
//         }
//       }
//     }
//   }
//   console.log("numero de operações", operations);
//   return operations;
// }

// console.log("caso 1 --->", GetOptimalContentStorage([1, 0, 1, 0, 1]));
// console.log("caso 2 --->", GetOptimalContentStorage([1, 0, 0, 1, 1, 0]));
// console.log("caso 3 --->", GetOptimalContentStorage([1, 0, 0, 0, 1]));
// console.log("caso 4 --->", GetOptimalContentStorage([0, 1, 1, 0, 0, 1]));

// console.log(
//   "caso 5 --->",
//   GetOptimalContentStorage([1, 0, 0, 1, 1, 0, 0, 0, 1])
// );

// function main() {
//   const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

//   const tiktokStorageCount = parseInt(readLine().trim(), 10);

//   let tiktokStorage = [];

//   for (let i = 0; i < tiktokStorageCount; i++) {
//     const tiktokStorageItem = parseInt(readLine().trim(), 10);
//     tiktokStorage.push(tiktokStorageItem);
//   }

//   const result = GetOptimalContentStorage(tiktokStorage);

//   ws.write(result + "\n");

//   ws.end();
// }
