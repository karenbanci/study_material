/*https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.*/

var isValid = function (s) {
  const array = s.split("");
  console.log(array);

  let arrayAbertos = [];

  for (let i = 0; i < array.length; i++) {
    let caracterAtual = array[i];
    if (
      caracterAtual === "(" ||
      caracterAtual === "{" ||
      caracterAtual === "["
    ) {
      arrayAbertos.push(caracterAtual);
      console.log("inclui os abertos", arrayAbertos);

    } else {
      const arrayUltimoAberto = arrayAbertos[arrayAbertos.length - 1];
      console.log("ultimo abertooooo ----", arrayUltimoAberto);

      let fechadorDoUltimoAberto;

      if (arrayUltimoAberto === "(") {
        fechadorDoUltimoAberto = ")";
      }

      if (arrayUltimoAberto === "{") {
        fechadorDoUltimoAberto = "}";
      }

      if (arrayUltimoAberto === "[") {
        fechadorDoUltimoAberto = "]";
      }

      if (caracterAtual === fechadorDoUltimoAberto) {
        arrayAbertos.pop();
        console.log("atual abertos *******", arrayAbertos);
      } else {
        return false;
      }
    }
  }
  if(arrayAbertos.length == 0){
    return true;
  } else {
    return false;
  }
};

const s = "(";
console.log(isValid(s));

// if(array[i] === ")" || array[i] === '}' || array[i] === ']') {
//   arrayFechados.push(array[i]);
//   console.log("inclui os fechados", arrayFechados)
// }

// const arrayUltimoFechado = arrayFechados[arrayFechados.length -1];
// console.log('ultimo fechadooooo ----', arrayUltimoFechado);
