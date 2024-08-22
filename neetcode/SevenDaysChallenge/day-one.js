/**
 * Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

arr = [1,1,0,-1,-1]
There are 5 elements, two positive, two negative and one zero. Their ratios are , 2/5 = 0.400000 ,2/5 = 0.400000 and 1/5 = 0.200000
Results are printed as:

0.400000
0.400000
0.200000
 */
// function plusMinus(arr) {
//   // Write your code here
//   let positive = 0;
//   let negative = 0;
//   let zero = 0;
//   let len = arr.length;

//   for (let char in arr) {
//     // console.log("arr[char]", arr[char]);
//     if (arr[char] < 0) {
//       negative++;
//       // console.log("negative", negative);
//     } else if (arr[char] === 0) {
//       zero++;
//       // console.log("zero", zero);
//     } else {
//       positive++;
//       // console.log("positive", positive);
//     }
//   }

//   positive = (positive / len).toFixed(6);
//   negative = (negative / len).toFixed(6);
//   zero = (zero / len).toFixed(6);

//   console.log("positive", positive);
//   console.log("negative", negative);
//   console.log("zero", zero);

// }

// plusMinus([1, 1, 0, -1, -1]);
// plusMinus([-4, 3, -9, 0, 4, 1]);

/**
 Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

 eg:
len: 5 elements
arr [ 1, 3, 5, 7, 9]
output = 16 24

the min sum: 1+3+5+7 = 16
the max sum: 3+5+7+9 = 24
the max sum elements = 4

identificar o maior valor entre os elementos
maior = 9
menor = 1

entao na hora da soma, ignorar o valor de maior elemento e o de menor elemento

 */

// function miniMaxSum(arr) {
//   // Write your code here
//   const n = arr.length;
//   arr.sort((a, b) => a - b);

//   const minSum = arr.slice(0, n - 1).reduce((acc, curr) => {
//     return acc + curr;
//   });
//   const maxSum = arr.slice(1).reduce((acc, curr) => {
//     return acc + curr;
//   });

//   console.log(minSum, maxSum);
// }
// miniMaxSum([1, 9, 3, 7, 5]);

/**
 Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
 */

// function timeConversion(s) {
//   // Extraímos os elementos importantes
//   const final = s.slice(-2); // AM ou PM
//   let hour = parseInt(s.slice(0, 2)); // Hora inicial em formato numérico
//   const rest = s.slice(2, 8); // Minutos e segundos

//   if (final === "PM" && hour !== 12) {
//     hour += 12;
//   } else if (final === "AM" && hour === 12) {
//     hour = 0;
//   }

//   // Formata a hora para garantir que tenha dois dígitos
//   const hourStr = hour.toString().padStart(2, "0");

//   // Retorna a string no formato de 24 horas
//   return hourStr + rest;
// }
// timeConversion("12:01:00PM");
// timeConversion("03:20:00PM");
// timeConversion("10:20:00PM");
// timeConversion("12:20:00AM");
// timeConversion("06:43:03AM");
