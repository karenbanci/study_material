/**
 * Task

We provide the implementation for a Rectangle class in the editor. Perform the following tasks:

Add an area method to Rectangle's prototype.
Create a Square class that satisfies the following:
It is a subclass of Rectangle.
It contains a constructor and no other methods.
It can use the Rectangle class' area method to print the area of a Square object.
Locked code in the editor tests the class and method implementations and prints the area values to STDOUT.
 */

// class Rectangle {
//   constructor(w, h) {
//     this.w = w;
//     this.h = h;
//   }
// }
// /*
//  *  Write code that adds an 'area' method to the Rectangle class' prototype
//  */
// Rectangle.prototype.area = function () {
//   return this.w * this.h;
// };
// const retangulo = new Rectangle(3, 4);
// console.log(retangulo.area());

// /*
//  * Create a Square class that inherits from Rectangle and implement its class constructor
//  */
// class Square extends Rectangle {
//   constructor(side) {
//     super(side, side);
//   }
// }
// const rec = new Rectangle(3, 3);
// console.log(rec.area());

/**
 * Task

The code in the editor has a tagged template literal that passes the area and perimeter of a rectangle to a tag function named sides. Recall that the first argument of a tag function is an array of string literals from the template, and the subsequent values are the template's respective expression values.

Complete the function in the editor so that it does the following:

Finds the initial values of  and  by plugging the area and perimeter values into the formula:
where  is the rectangle's area and  is its perimeter.
Creates an array consisting of  and  and sorts it in ascending order.
Returns the sorted array.
Input Format

The first line contains an integer denoting .
The second line contains an integer denoting .

Constraints

Output Format

Return an array consisting of  and , sorted in ascending order.

Sample Input 0

10
14
Sample Output 0

10
14
 */
// function sides(literals, ...expressions) {
//   const [A, P] = [...expressions];
//   // console.log("The area is: ", A, ".\nThe perimeter is: ", P, ".");

//   const s1 = (P + Math.sqrt(P * P - 16 * A)) / 4;
//   const s2 = (P - Math.sqrt(P * P - 16 * A)) / 4;

//   return [s1, s2].sort((a, b) => a - b);
// }
// // Example usage with the provided inputs
// const expressions = [140, 48]; // Area = 140, Perimeter = 48
// const literals = ["The area is: ", ".\nThe perimeter is: ", "."];

// console.log(sides(literals, ...expressions)); // Output: [10, 14]

/**
 * Task

Complete the function in the editor. It has one parameter: an array, . It must iterate through the array performing one of the following actions on each element:

If the element is even, multiply the element by .
If the element is odd, multiply the element by .
The function must then return the modified array.

Input Format

The first line contains an integer, , denoting the size of .
The second line contains  space-separated integers describing the respective elements of .

Constraints

, where  is the  element of .
Output Format

Return the modified array where every even element is doubled and every odd element is tripled.

Sample Input 0

5
1 2 3 4 5
Sample Output 0

3 4 9 8 15
 */

// function modifyArray(nums) {
//   for (let i = 0; i < nums.length; i++) {
//     if (nums[i] % 2 === 0) {
//       console.log("par", nums[i]);
//       nums[i] = nums[i] * 2;
//     } else {
//       nums[i] = nums[i] * 3;
//       console.log("impar", nums[i]);
//     }
//   }
//   return nums;
// }
// console.log(modifyArray([1, 2, 3, 4, 5]));
