/* You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer.
----------------------------------------------------
Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, rrecord is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30. */

// vamos definir a pilha

function Stack() {
  this.items = [];
  console.log(`---o stack é: ${this.items}`);

  this.push = function (element) {
    // adicionar um novo item a pilha
    this.items.push(element);
  };

  this.pop = function () {
    // remover o item do topo da pilha
    return this.items.pop();
  };

  this.peek = function () {
    // devolve o element que está no topo da pilha
    return this.items[this.items.length - 1];
  };

  this.peek2 = function () {
    // devolve o element que está no segundo valor da pilha
    return this.items[this.items.length - 2];
  };
}

const calPoints = function (ops) {
  let stack = new Stack();

  console.log(`este é a array ${ops}`);

  for (let i = 0; i < ops.length; i++) {
    console.log(`o stack é: ${stack.items}`);
    console.log(`o atual é: ${ops[i]}`);

    if (ops[i] === "C") {
      let removedPoint = stack.pop();
      console.log(`item removido ${removedPoint}`);
      // stack += removedPoint
    } else if (ops[i] === "D") {
      let doublePoint = stack.peek() * 2;
      console.log(`dobro do ultimo valor ${doublePoint}`);
      stack.push(doublePoint);
    } else if (ops[i] === "+") {
      let sumPoint = stack.peek() + stack.peek2();
      console.log(`soma de pontos ${sumPoint}`);
      stack.push(sumPoint);
    } else {
      stack.push(parseInt(ops[i]));
    }
  }
  const meLigaDeVolta = (a, b) => {
    console.log(`somando ${a} e adicionando para ${b}`);
    return a + b;
  };
  return stack.items.reduce(meLigaDeVolta, 0);
};

// exemplo 1
let exemplo1 = ["5", "2", "C", "D", "+"];
// let exemplo1 = ["5","C"];

console.log(calPoints(exemplo1));
