/**
 * Task

We define  to be a sequence of distinct sequential integers from  to ; in other words, . We want to know the maximum bitwise AND value of any two integers,  and  (where ), in sequence  that is also less than a given integer, .

Complete the function in the editor so that given  and , it returns the maximum .

Note: The  symbol represents the bitwise AND operator.

Input Format

The first line contains an integer, , denoting the number of function calls.
Each of the  subsequent lines defines a dataset for a function call in the form of two space-separated integers describing the respective values of  and .

Constraints

Output Format

Return the maximum possible value of  for any  in sequence .

Sample Input 0

3
5 2
8 5
2 2
Sample Output 0

1
4
0
 */
// function getMaxLessThanK(arr) {
//   // console.log(arr);
//   let max = 0;
//   let arrMax = [];
//   let s = [];

//   for (let i = 0; i < arr.length; i++) {
//     let call = arr[i];
//     let n = call[0];
//     let k = call[1];
//     max = 0;
//     console.log("----------------call", call, "-------n", n, "------k", k);
//     for (let a = 1; a <= n; a++) {
//       console.log("a ====>", a);
//       s.push(a);
//       // console.log(s);
//       for (let b = a + 1; b <= n; b++) {
//         console.log("b------->", b);
//         let bit = a & b;
//         console.log("bit", bit, "k", k);
//         if (bit < k && bit > max) {
//           max = bit;
//           console.log("guardando o máximo", max);
//         }
//       }
//     }
//     arrMax.push(max);
//   }
//   console.log(s);
//   console.log("arrMax===============", arrMax);
// }
// const arr = [
//   [5, 2],
//   [8, 5],
//   [2, 2],
// ];
// console.log(getMaxLessThanK(arr));
// const a = 3;
// const b = 2;
// console.log(a & b);
