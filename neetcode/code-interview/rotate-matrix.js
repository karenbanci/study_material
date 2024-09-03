/**
 * Given a image represented by an N X N matrix, where each pixel in the image is
 * represented by an integer. Write a method to rotate the image by 90 degrees. Can you do this in place?
 *
 * # 51. Think about layer by layer. Can you rotate specific layer?
 * # 100. swapping the values in four arrays.
 */

function rotateMatrix(matrix) {
  let rotated = [];
  // console.log(matrix.length);
  //
  for (let j = 0; j < matrix.length; j++) {
    let subArr = new Array();
    for (let i = matrix.length - 1; i >= 0; i--) {
      // console.log("j", j);
      // console.log("i", i, "j", j, "column", matrix[i][j]);
      subArr.push(matrix[i][j]);
    }
    rotated.push(subArr);
  }
  console.log(rotated);
}

const matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
];
console.log(rotateMatrix(matrix));
