function isDifferent(index, curr) {
  console.log("isDifferent index e curr", index, curr);
  return index !== curr ? true : false;
}

// console.log(isDifferent(1, 1));
// console.log(isDifferent(1, 2));

// compara o ponteiro atual se existe na nova string
function currExist(str, currLetter) {
  console.log("currExist", str);
  const newSet = new Set(str);

  return newSet.has(currLetter) ? true : false;
}

// console.log(currExist("a", "a")); // true
// console.log(currExist("o", "o")); // true
// console.log(currExist("cdefss", "b")); // false
// console.log(currExist("aadfge", "j")); // false
// console.log(currExist("lsff", "a")); // false

// function stringCompression(str) {
//   let count = 0;
//   let index = 0;
//   let size = 1;
//   // let output = `${str[curr]}${count}`;
//   let output = "";
//   let strLen = str.length;

//   // condicao para parar o loop
//   for (let curr = 0; curr < strLen; curr++) {
//     console.log(
//       `30:: index ${index} = ${str[index]}    curr ${curr} = ${str[curr]}`
//     );

//     // curr exite no output ? NAO
//     if (!output[curr]) {

//       // é diferente? SIM
//       console.log("40:: curr existe?   NAO");

//       if (isDifferent(str[index], str[curr])) {
//         console.log("é diferente?   SIM");
//         console.log("curr exite ? NAO     é diferente? SIM");
//         console.log(
//           `40:: index ${index} = ${str.charAt(index)}    curr ${curr} = ${
//             str[curr]
//           }`
//         );

//         count = 1;
//         size++;
//         curr++;
//         // index = curr;
//         console.log("count", count, "tamanho", size, "index", index);
//         console.log("32:: saída", output, "\n");

//       } else {
//         // é diferente? NAO

//         console.log(" é diferente? NAO");
//         count++;
//         output += `${count}`;
//       }

//       // curr existe ? SIM
//     } else {
//       console.log("64:: curr existe?   SIM");
//       // é diferente? NAO
//       if (isDifferent(str[index], str[curr]) === false) {

//         console.log("72:: curr existe ? SIM     é diferente? NAO");
//         console.log("61: count", count, "tamanho", size, "curr", curr);
//         count++;
//         size++;
//         curr++;
//         console.log("65: count", count, "tamanho", size, "curr", curr);
//         console.log("44: saída", output, "\n");
//       }
//       console.log("68::  curr existe ? SIM     é diferente? SIM");
//       count = 1;
//       output += `${str[curr]}${count}`;
//       size++;
//       index = curr;
//       // curr++;
//     }
//   }
//   console.log("                    output", output);

//   // console.log("tamanho da string", stopLoop + index);
// }

// stringCompression("aabcccccaaa");

// BOOK SOLUTION
// function stringCompression(str) {
//   // check final length and return input string if it would be longer
//   let finalLength = countCompression(str);
//   if (finalLength >= str.length) return str;

//   // initial capacity
//   let compressed = new String(finalLength);
//   console.log("87:: compressed", compressed);
//   let countConsecutive = 0;
//   console.log("89:: countConsecutive", countConsecutive);

//   for (let i = 0; i < str.length; i++) {
//     countConsecutive++;
//     console.log("94:: countConsecutive", countConsecutive);

//     // if next char is different than curr, append this char to result
//     if (i + 1 >= str.length || str.charAt(i) != str.charAt(i + 1)) {
//       compressed.concat(str.charAt(i));
//       compressed.concat(countConsecutive);
//       countConsecutive = 0;
//     }
//   }

//   console.log("103:: compressed.toString()", compressed.toString());

//   return compressed.toString();
// }

// function countCompression(str) {
//   let compressedLength = 0;
//   let countConsecutive = 0;

//   for (let i = 0; i < str.length; i++) {
//     countConsecutive++;

//     // if next char is different than curr, increase the length
//     if (i + 1 >= str.length || str.charAt(i) != str.charAt(i + 1)) {
//       compressedLength += 1 + countConsecutive.valueOf().length;
//       countConsecutive = 0;
//       console.log("119:: compressedLength", compressedLength);
//     }
//   }
//   console.log("122:: compressedLength", compressedLength);

//   return compressedLength;
// }

function stringCompression(str) {
  let output = "";
  let outLetter = "";
  let count = 1;
  // let len = output.length;

  for (let i = 0; i < str.length; i++) {
    // console.log("output len", len);
    let currLetter = str[i];
    // console.log("letra atual:", currLetter, "\nsaida letra:", outLetter);
    // output = `${currLetter}`;

    // é igual
    if (currLetter == outLetter) {
      output = output.substring(0, output.length - 1);
      count++;

      // não é igual
    } else {
      output += `${currLetter}`;
      count = 1;
    }
    outLetter = currLetter;
    output += `${count}`;
  }
  return output;
}

// stringCompression("aa");
// stringCompression("aab");
// stringCompression("aabcc");
console.log(stringCompression("aabcccccaaa")); // a2b1c5a3
