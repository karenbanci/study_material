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
s consists of parentheses only '()[]{}'.

1a iteração - hashMap[s[i]] - s[0] = "("
  ele vai adicionar o valor da abertura no stack
      stack.push(hashMap[s[0]]);
      stack = [")"]

2a iteração - hashMap[s[i]] - s[1] = ")"
      else if (stack.length > 0 && stack[stack.length - 1] === s[i])
      else if (1 > 0 && stack[1-1] === s[1])
      else if (1 > 0 && stack[0] === s[1]) - sim
      stack.pop()

3a iteração - hashMap[s[i]] - s[2] = "["
  ele vai adicionar o valor da abertura no stack
      stack.push(hashMap[s[2]]);
      stack = ["]"]

4a iteração - hashMap[s[i]] - s[3] = "]"
      else if (stack.length > 0 && stack[stack.length - 1] === s[i])
      else if (1 > 0 && stack[1-1] === s[3])
      else if (1 > 0 && stack[0] === s[3]) - sim
      stack.pop()

5a iteração - hashMap[s[i]] - s[4] = "{"
  ele vai adicionar o valor da abertura no stack
      stack.push(hashMap[s[4]]);
      stack = ["{"]

6a iteração - hashMap[s[i]] - s[5] = "}"
      else if (stack.length > 0 && stack[stack.length - 1] === s[i])
      else if (1 > 0 && stack[1-1] === s[5])
      else if (1 > 0 && stack[0] === s[5]) - sim
      stack.pop()

retornou true

*/

var isValid = function (s) {
  const hashMap = {"(": ")", "{": "}", "[": "]",};
  let stack = [];

  for(let i = 0; i < s.length; i++){

    if(hashMap[s[i]]){
      // s[i] é o bracket de abertura
      stack.push(hashMap[s[i]]);
    } else if (stack.length > 0 && stack[stack.length - 1] === s[i]){
      // s[i] fechando o bracket e o top do bracket estiver combinando
      stack.pop()
    } else {
      //s[i] fechando o bracket e o top do nao da match
      return false
    }
  }

 return true
};

const s = "([]){}";
console.log(isValid(s));

      // console.log("abertura: " + arrayAbertos + "fechamento:  " + fechamento);
