/**
 * Function Description

Complete the getSecondLargest function in the editor below.

getSecondLargest has the following parameters:

int nums[n]: an array of integers
Returns

int: the second largest number in
Input Format

The first line contains an integer, , the size of the  array.
The second line contains  space-separated numbers that describe the elements in .

Constraints

, where  is the number at index .
The numbers in  may not be distinct.
Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
 */
// function getSecondLargest(nums) {
//   let secondMax = 0;
//   let max = 0;
//   // Complete the function
//   for (let i = 0; i < nums.length; i++) {
//     // console.log(nums[i]);
//     console.log("nums[i]", nums[i]);
//     if (nums[i] > max) {
//       secondMax = max;
//       max = nums[i];
//       console.log(
//         " substituindo o maximo linha 38 max",
//         max,
//         "secondMax",
//         secondMax
//       );
//     } else if (nums[i] < max && nums[i] > secondMax) {
//       secondMax = nums[i];
//       console.log("substituind o secondMax nums[i]", nums[i]);
//     }
//   }
//   console.log("secondMax", secondMax);
//   return secondMax;
// }
// console.log(getSecondLargest([2, 3, 6, 6, 5, 1]));
// console.log(getSecondLargest([2, 3, 5, 6, 27, 2, 32]));
// console.log(getSecondLargest([5]));

/**
 * ask

Complete the reverseString function; it has one parameter, . You must perform the following actions:

Try to reverse string  using the split, reverse, and join methods.
If an exception is thrown, catch it and print the contents of the exception's  on a new line.
Print  on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.
Input Format

Locked stub code in the editor reads variable  from stdin and passes it to the function.

Output Format

You must write two print statements using console.log():

Print the contents of a caught exception's  on a new line. If no exception was thrown, this line should not be printed.
Print  on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.
Sample Input 0

"1234"
Sample Output 0

4321
 */
// function reverseString(s) {
//   try {
//     s = s.split("").reverse().join("");
//   } catch (e) {
//     console.log(e.message);
//     // body of catch
//   } finally {
//     console.log(s);
//   }
// }
// // console.log(reverseString("1234"));
// console.log(reverseString(Number(1234)));

/**
 * Task

Complete the isPositive function below. It has one integer parameter, . If the value of  is positive, it must return the string YES. Otherwise, it must throw an Error according to the following rules:

If  is , throw an Error with  Zero Error.
If  is negative, throw an Error with  Negative Error.
Input Format

Locked stub code in the editor reads the following input from stdin and passes each value of  to the function as an argument:
The first line is an integer, , denoting the number of times the function will be called with some .
Each line  of the  subsequent lines contains an integer denoting some .

Constraints

Output Format

If the value of  is positive, the function must return the string YES. Otherwise, it must throw an Error according to the following rules:

If  is , throw an Error with  Zero Error.
If  is negative, throw an Error with  Negative Error.
Sample Input 0

3
1
2
3
Sample Output 0

YES
YES
YES
 */

// function isPositive(a) {
//   if (a > 0) {
//     return "YES";
//   } else if (a === 0) {
//     throw new Error("Zero Error");
//   } else {
//     throw new Error("Negative Error");
//   }
// }

// console.log(isPositive(1));
// console.log(isPositive(-1));
// console.log(isPositive(0));
// console.log(isPositive(6));
// console.log(isPositive(-2));

/**
 * Task

Complete the function in the editor. It has two parameters:  and . It must return an object modeling a rectangle that has the following properties:

length : This value is equal to a.
width : This value is equal to b.
perimeter: This value is equal to 2*(a+b)
area : This value is equal to a*b
Note: The names of the object's properties must be spelled correctly to pass this challenge.

Input Format

The first line contains an integer denoting .
The second line contains an integer denoting .

Constraints

Output Format

Return a object that has the properties specified above. Locked code in the editor prints the returned object's , , , and  to STDOUT.

Sample Input 0

4
5
Sample Output 0

4
5
18
20
 */

// function Rectangle(a, b) {
//   const object = {
//     length: a,
//     width: b,
//     perimeter: 2 * (a + b),
//     area: a * b,
//   };

//   return object;
// }
// console.log(Rectangle(4, 5));
// console.log(Rectangle(7, 21));
