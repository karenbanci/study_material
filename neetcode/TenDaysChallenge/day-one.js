/**
 *   3) Calculate the area of a rectangle.
 *
 *   length: The length of the rectangle.
 *   width: The width of the rectangle.
 *
 *	Return a number denoting the rectangle's area.
//  **/
// function getArea(length, width) {
//   let area;
//   // Write your code here
//   area = length * width;

//   return area;
// }

/**
 *   Calculate the perimeter of a rectangle.
 *
 *	length: The length of the rectangle.
 *   width: The width of the rectangle.
 *
 *	Return a number denoting the perimeter of a rectangle.
 **/
// function getPerimeter(length, width) {
//   let perimeter;
//   // Write your code here
//   perimeter = (length + width) * 2;

//   return perimeter;
// }

// const length = 3;
// const width = 4.5;
// console.log(getArea(length, width));
// console.log(getPerimeter(length, width));

/**
 Task

Implement a function named factorial that has one parameter: an integer, . It must return the value of  (i.e.,  factorial).

Input Format

Locked stub code in the editor reads a single integer, , from stdin and passes it to a function named factorial.

Constraints

Output Format

The function must return the value of .

Sample Input 0

4
Sample Output 0

24
 */

// function factorial(n) {
//   let countDown = n;
//   let result = 1;

//   while (countDown > 0) {
//     result *= countDown;
//     console.log("result", result, "n", n, "countDown", countDown);
//     countDown--;
//   }
//   return result;
// }
// console.log(factorial(4));

/**
 * Task

Declare a constant variable, , and assign it the value Math.PI. You will not pass this challenge unless the variable is declared as a constant and named PI (uppercase).
Read a number, , denoting the radius of a circle from stdin.
Use  and  to calculate the  and  of a circle having radius .
Print  as the first line of output and print  as the second line of output.
Input Format

A single integer, , denoting the radius of a circle.

Constraints

 is a floating-point number scaled to at most  decimal places.
Output Format

Print the following two lines:

On the first line, print the  of the circle having radius .
On the second line, print the  of the circle having radius .
Sample Input 0

2.6
Sample Output 0

21.237166338267002
16.336281798666924
 */
// const PI = Math.PI;

// // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
// const input = 2.6;

// // Print the area of the circle:
// const circleArea = PI * input ** 2;
// console.log(circleArea);

// // Print the perimeter of the circle:
// const circlePerimeter = 2 * PI * input;
// console.log(circlePerimeter);
