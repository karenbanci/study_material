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

  let array = s.split('');
  console.log('nova array', array);

  for (var i = 0; i < array.length; i++) {

    let atual = array[i];
    // let aberto = '';
    // let fechamentoDoUltimoAberto = [];


    if (atual === "(" || atual === "[" || atual === "{") {
      // aberto.push(atual);
      // console.log('aberto', aberto);

      if (atual === "(") {
        console.log("nova atual", atual);
        if (fechamento === ")") {
          console.log("nova fechamento", fechamento);
          return true;
        }
      } else if (atual === "[") {
        console.log("nova atual", atual);

        if (fechamento === "]") {
          console.log("nova fechamento", fechamento);

          return true;
        }
      } else if (atual === "{") {
        console.log("nova atual", atual);

        if (fechamento === "}") {
          console.log("nova fechamento", fechamento);

          return true;
        }
      }

    }
    if(array.length === 0) {
      return true;
    } else {
      return false;
    }
  }
}

const s = "(){}[]";
console.log(isValid(s));
