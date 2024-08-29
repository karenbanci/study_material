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

//   // vertical
//   for (let j = 0; j < grid[0].length; j++) {
//     for (let i = 0; i < grid.length - 1; i++) {
//       console.log("i", i, "--------j", j);
//       const s1 = grid[i][j];
//       const s2 = grid[i + 1][j];
//       console.log("s1", s1, "s2", s2);

//       if (s1 > s2) {
//         console.log("NO");
//         return "NO";
//       }
//     }
//   }
//   console.log("YES");
//   return "YES";
// }

// const grid = ["abc", "hjk", "mpq", "rtv"]; // YES
// // const grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]; // YES
// // const grid = ["xywuv", "ebacd", "fghij", "olmkn", "trpqs"]; // NO
// gridChallenge(grid);

// function superDigit(n, k) {
//   let p = sum(n);
//   return sum((p * k).toString());
// }

// function sum(p) {
//   while (p.length > 1) {
//     let newArr = p.split("");
//     let n = newArr.reduce((sum, curr) => sum + parseInt(curr), 0);
//     p = n.toString();
//   }
//   return p;
// }

// // console.log('FINAL', superDigit("9875", 4)) // 8
// console.log(
//   "FINAL",
//   superDigit(
//     "7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153",
//     100000
//   )
// );
// a = Math.floor(19/10)
// console.log(a)
