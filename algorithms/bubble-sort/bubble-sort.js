const swap = require("./swap");

const bubbleSort = (input) => {
  // nossa array de entrada ainda pode não estar classificado e precisar de trocas adicionais de elementos e depois mudaremos para false, ou seja, o array de entrada não precisa mais trocar para classificá-lo.
  let swapping = true;
  let swapCount = 0;

  while (swapping) {
    swapping = false;
    for (let i = 0; i < input.length - 1; i++) {
      if (input[i] > input[i + 1]) {
        // console.log(input)
        // console.log(`Swapping pair ${input[i]}, ${input[i + 1]} in [${input}]`);
        swap(input, i, i + 1);
        swapCount++;
        swapping = true;
      }
    }
  }
  console.log(`Swapped ${swapCount} times`);
  return input;
};

module.exports = bubbleSort;

console.log(bubbleSort([3, 2, 1]));
