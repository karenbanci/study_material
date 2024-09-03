/**
 * entrada = "aaab", 3
 * saida  = [aaa]b
 *
 * * entrada = "caaaa", 4
 * saida  = c[aaaa]
 *
 *  * * entrada = "caabb", 2
 * saida  = erro
 */

/**
 * input = ["cat", "dog", "karen", "honorio"]
 * output: ["cg", "de", "dn", "ht"]
 */

// function firstLast(arr) {
//   let str = "";
//   let result = [];

//   for (let w = 0; w < arr.length; w++) {
//     let word1 = arr[w];
//     let word2 = arr[w + 1];

//     if (!word2) {
//       word2 = arr[0];
//     }

//     // console.log("palavra", word1);
//     str = `${word1[0]}${word2[word2.length - 1]}`;
//     // console.log("testando ....", str);

//     result.push(str);
//   }
//   console.log(result);
// }
// firstLast(["cat", "dog", "karen", "honorio"]);
