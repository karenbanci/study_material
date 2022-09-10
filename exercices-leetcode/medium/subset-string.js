function subsetA(arr) {
  // Write your code here

  const arrayInOrder = arr.sort();
  console.log("ordenado: " + arrayInOrder);
  const initialValue = 0;
  const sum = arr.reduce((prev, curr) => prev + curr, initialValue);
  console.log(sum);

  let arrayA = [];

  for (let i = 0; i < arrayInOrder.length - 1; i++) {
    for (let j = 1; j < arrayInOrder.length; j++) {
      if (arrayInOrder[i] != arrayInOrder[j]) {
        const comparativeA = arrayInOrder[i] + arrayInOrder[j];
        const comparativeB = sum - comparativeA;
        // console.log(
        //   "resultado: " +
        //     sum +
        //     " - " +
        //     (arrayInOrder[i] + arrayInOrder[j] + " = " + comparativeB)
        // );

        // console.log("subtraido: " + comparativeB);

        if (comparativeA > comparativeB) {
          console.log(
            "adicionando: " + (arrayInOrder[i] + " - " + arrayInOrder[j])
          );
          if (arrayA.length) {
            if (sum > arrayA[0] + arrayA[1]) {
              arrayA = [arrayInOrder[i], arrayInOrder[j]];
            }
          } else {
            arrayA.push(arrayInOrder[i], arrayInOrder[j]);
          }
        }
      }
    }
  }
  return arrayA;
}

//  output = [4,5]
// const entrada = [5, 3, 2, 4, 1, 2];
// console.log(subsetA(entrada));

console.log("-------------------");
//  output = [5,6]
// const entrada2 = [4, 2, 5, 1, 6];
// console.log(subsetA(entrada2));

console.log("-------------------");
//  output = [8,8,9,10,10,10,10]
const entrada3 = [20, 2, 3, 4, 4, 5, 9, 7, 8, 6, 10, 4, 5, 10, 10, 8, 4, 6, 4, 10 ,1];
console.log(subsetA(entrada3));

console.log("-------------------");
//  output = [34,35,35,37,37,38,38,39,40,41,43,43,44,45,45,45,45,45,45,46,46,46,46,47,47,47,50,50]
const entrada4 = [
  97, 8, 34, 40, 2, 2, 22, 32, 22, 3, 32, 7, 31, 16, 29, 22, 46, 45, 10, 45, 46,
  45, 23, 16, 4, 45, 12, 5, 39, 45, 4, 47, 31, 1, 7, 35, 12, 27, 8, 46, 47, 50,
  27, 14, 26, 11, 20, 45, 15, 38, 24, 10, 13, 6, 6, 9, 17, 13, 28, 43, 41, 33,
  46, 17, 21, 25, 4, 9, 3, 32, 33, 4, 50, 24, 30, 37, 27, 34, 13, 15, 9, 37, 26,
  38, 16, 19, 47, 3, 43, 22, 13, 28, 17, 23, 35, 44, 17, 32,
];
console.log(subsetA(entrada4));
