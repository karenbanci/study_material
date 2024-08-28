/**
 * Given an array of integers, where all elements but one occur twice, find the unique element.

Example = [1,2,3,4,3,2,1]

The unique element is 4.
 */
// function lonelyinteger(a) {
//   // Write your code here
//   // colocar em um set e separar quem estiver duplicado

//   const arrSet = new Set();
//   const duplicate = new Set();

//   for (let num of a) {
//     if (arrSet.has(num)) {
//       duplicate.add(num);
//     } else {
//       arrSet.add(num);
//     }
//   }
//   console.log(arrSet, duplicate);

//   duplicate.forEach((element) => arrSet.delete(element));
//   console.log(arrSet, duplicate);

//   let unique = "";

//   for (let i = a.length - 1; i >= 0; i--) {
//     if (arrSet.has(a[i])) {
//       unique = a[i];
//       break;
//     }
//   }
//   console.log(unique);
//   return unique;
// }
// lonelyinteger([1, 2, 3, 4, 3, 2, 1]);

/**Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix

1 2 3
4 5 6
9 8 9

1+5+9 = 15
3+5+9 = 17

| 15 - 17 | = 2
*/

// function diagonalDifference(arr) {
//   // Write your code here
//   let left = 0;
//   let right = 0;

//   for (let i = 0; i < arr.length; i++) {
//     left += arr[i][i];
//     let j = arr.length - i - 1;
//     right += arr[i][j];
//     console.log("left =>", left, "right => ", right);
//   }
//   //

//   // console.log(result)
//   let result = Math.abs(left - right);
//   console.log(result);
//   return result;
// }

// diagonalDifference([
//   [1, 2, 3],
//   [4, 5, 6],
//   [9, 8, 9],
// ]);

// diagonalDifference([
//   [6, 6, 7, -10, 9, -3, 8, 9, -1],
//   [9, 7, -10, 6, 4, 1, 6, 1, 1],
//   [-1, -2, 4, -6, 1, -4, -6, 3, 9],
//   [-8, 7, 6, -1, -6, -6, 6, -7, 2],
//   [-10, -4, 9, 1, -7, 8, -5, 3, -5],
//   [-8, -3, -4, 2, -3, 7, -5, 1, -5],
//   [-2, -7, -4, 8, 3, -1, 8, 2, 3],
//   [-3, 4, 6, -7, -7, -8, -3, 9, -6],
//   [-2, 0, 5, 4, 4, 4, -3, 3, 0],
// ]);

/**
        Chat GPT
 Key Points:
Comparison Sorting:
Quicksort is a common comparison sorting algorithm with a running time of n×log(n) n×log(n) in the worst case.
No comparison sort algorithm can have a better time complexity than n×log(n) n×log(n) because this represents the minimum number of comparisons required to place each element correctly.
Alternative Sorting:
Counting Sort is an example of a non-comparison sorting algorithm.
It works by creating an array of counters that cover the entire range of values in the input array.
Each time a value occurs, its corresponding counter is incremented.
Finally, the counting array is used to reconstruct the sorted array.
Example Provided:
Given an array arr = [1, 1, 3, 2, 1], a counting array is created to count occurrences.
The example shows how the array evolves after each iteration of incrementing the counting array.
This technique is particularly efficient when the range of input values is not significantly larger than the number of elements in the array, making it faster than comparison-based sorting in certain scenarios
 */
// function countingSort(arr) {
//   const maxValue = 100;
//   const frequency = new Array(maxValue).fill(0);

//   for (let i = 0; i < arr.length; i++) {
//     frequency[arr[i]]++;
//     console.log(arr[i], frequency[arr[i]]);
//   }
//   return frequency;
// }

// // Test the function
// const output = countingSort([1, 1, 3, 2, 1]);
// console.log(output); // Expected output: [1, 1, 1, 2, 3]

// Final test
/**
 * function flippingMatrix(matrix) {
    // Write your code here
    let columnValues = matrix.map(row => row[2]);
    columnValues.reverse();

    for (let i = 0; i < matrix.length; i++) {
        matrix[i][2] = columnValues[i];
    }



    let rowValues = matrix[0];
    console.log(rowValues)

    for (let i = 0; i < rowValues.length/2; i++) {
        let left = rowValues.length - i - 1
        // console.log(left)
        let temp = rowValues[i]
        rowValues[i] = rowValues[left]
        rowValues[left] = temp

        // console.log(rowValues)
    }
    // let rowValues = matrix.map(colum => colum[0])
        // matrix.reverse(matrix[0][i])

    console.log(matrix)


}

const matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]
 */
