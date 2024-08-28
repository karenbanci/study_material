/**
 * Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

Example

The grid is illustrated below.

a b c
a d e
e f g
The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

Function Description

Complete the gridChallenge function in the editor below.

gridChallenge has the following parameter(s):

string grid[n]: an array of strings
Returns

string: either YES or NO
Input Format

The first line contains , the number of testcases.

Each of the next  sets of lines are described as follows:
- The first line contains , the number of rows and columns in the grid.
- The next  lines contains a string of length

Constraints



Each string consists of lowercase letters in the range ascii[a-z]

Output Format

For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.

const grid = ['abc', 'hjk', 'mpq', 'rtv'] // YES
const grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'] // YES
const grid = ['xywuv', 'ebacd', 'fghij', 'olmkn', 'trpqs'] // NO
 */

// function gridChallenge(grid) {
//   // Write your code here
//   for (let i in grid) {
//     grid[i] = grid[i].split("").sort().join("");
//   }
//   console.log(grid);
//   console.log(grid[0][0], grid[1][0], grid[0][0] < grid[1][0]);
//   // colunas
//   for (let j = 0; j < grid[0].length; j++) {
//     // filas
//     for (let i = 0; i < grid.length - 1; i++) {
//       // console.log("i",i,  "j",j, "letra", grid[i][j])
//       console.log("i", i, "j", j);

//       const s1 = grid[i][j];
//       const s2 = grid[i + 1][j];
//       console.log("s1", s1, "< s2", s2);
//       if (s1 < s2) {
//         console.log("YES");
//         // console.log("*****")
//       } else {
//         console.log("NO");
//         return "No";
//       }
//     }
//   }
//   return "YES";
// }

// const grid = ["abc", "hjk", "mpq", "rtv"]; // YES
// // const grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]; // YES
// // const grid = ["xywuv", "ebacd", "fghij", "olmkn", "trpqs"]; // NO
// gridChallenge(grid);
