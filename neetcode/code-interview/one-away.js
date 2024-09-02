// Cracking code interview , page 91

// Karen's Solution
// function oneAway(strOne, strTwo) {
//   // console.log(strOne, ",", strTwo);
//   const setOne = new Set(strOne);
//   let away = 0;
//   // console.log(setOne);
//   // console.log("             ", strTwo);

//   for (let i = 0; i < strTwo.length; i++) {
//     // console.log("strTwo[i]", strTwo[i]);
//     if (!setOne.has(strTwo[i])) {
//       away++;
//     }
//   }

//   console.log("distancia", away);
//   if (away <= 1) {
//     console.log("true");
//     return true;4
//   } else {
//     console.log("false");
//     return false;
//   }
// }

// Book's Solution
function oneAway(strOne, strTwo) {
  // length checks
  if (strOne.length - strTwo.length > 1) {
    return false;
  }

  // get shorter and longer string
  const s1 = strOne.length < strTwo.length ? strOne : strTwo;
  const s2 = strOne.length < strTwo.length ? strTwo : strOne;

  let index1 = 0;
  let index2 = 0;
  let foundDifference = false;

  while (index2 < s2.length && index1 < s1.length) {
    // Dentro do loop, verificamos se os caracteres atuais das duas strings são diferentes.
    if (s1.charAt(index1) != s2.charAt(index2)) {
      //ensure that this is the first defference found
      if (foundDifference) return false;
      foundDifference = true;

      //Se as strings têm o mesmo comprimento, então a diferença foi causada por uma substituição de caractere. Neste caso, movemos o índice index1 para a próxima posição.
      if (s1.length == s2.length) {
        // on replace, move s1 pointer
        index1++;
      }
    } else {
      index1++; //if matching, move shorter pointer
    }
    index2++; // always move pointer for longer string
  }
  return true;
}

console.log(oneAway("pale", "ple")); // true
console.log(oneAway("pales", "pale")); // true
console.log(oneAway("pale", "bale")); // true
console.log(oneAway("pale", "bake")); // false
