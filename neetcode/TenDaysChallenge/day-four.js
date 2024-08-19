/**
 * Task

Complete the function in the editor. It has one parameter: an array, , of objects. Each object in the array has two integer properties denoted by  and . The function must return a count of all such objects  in array  that satisfy .

Input Format

The first line contains an integer denoting .
Each of the  subsequent lines contains two space-separated integers describing the values of  and .

Constraints

Output Format

Return a count of the total number of objects  such that . Locked stub code in the editor prints the returned value to STDOUT.

Sample Input 0

5
1 1
2 3
3 3
3 4
4 5
Sample Output 0

2
 */
// function getCount(objects) {
//   let count = 0;

//   for (let i = 0; i < objects.length; i++) {
//     const arr = Object.values(objects[i]);
//     console.log(arr[0], arr[1]);
//     if (arr[0] === arr[1]) {
//       count++;
//       console.log("count ======>", count);
//     }
//   }
//   console.log("total", count);
//   return count;
// }
// function getCount(objects) {
//   let counter = 0;

//   objects.forEach(({ x, y }) => {
//     if (x === y) counter++;
//   });

//   return counter;
// }

// const arr = [
//   // 5,
//   { x: 1, y: 1 },
//   { x: 2, y: 3 },
//   { x: 3, y: 3 },
//   { x: 3, y: 5 },
//   { x: 4, y: 5 },
// ];

// console.log(getCount(arr));

/**
 * Task

Create a Polygon class that has the following properties:

A constructor that takes an array of integer values describing the lengths of the polygon's sides.
A perimeter() method that returns the polygon's perimeter.
Locked code in the editor tests the Polygon constructor and the perimeter method.

Note: The perimeter method must be lowercase and spelled correctly.

Input Format

There is no input for this challenge.

Output Format

The perimeter method must return the polygon's perimeter using the side length array passed to the constructor.
 */

// class Polygon {
//   constructor(length) {
//     this.length = length;
//   }

//   // perimeter() {
//   //   let sum = 0;
//   //   for (let i = 0; i < this.length.length; i++) {
//   //     // console.log((sum += this.length[i]));
//   //     sum += this.length[i];
//   //   }
//   //   return sum;
//   // }

//   perimeter() {
//     return this.length.reduce((length, accum) => (accum += length), 0);
//   }
// }

// let triangle = new Polygon([3, 4, 5]);
// console.log(triangle.perimeter());
// When executed with a properly implemented Polygon class, this code should print the result of 4+3+5 = 12
