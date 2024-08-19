/**
 * Task

Complete the function in the editor below by returning a RegExp object, , that matches any string  that begins and ends with the same vowel. Recall that the English vowels are a, e, i, o, and u.

Constraints

The length of string  is  .
String  consists of lowercase letters only (i.e., [a-z]).
Output Format

The function must return a RegExp object that matches any string  beginning with and ending in the same vowel.

Sample Input 0

bcd
Sample Output 0

false

Sample Input 1

abcd
Sample Output 1

false
Explanation 1

This string ends in a consonant, so it cannot start and end with the same vowel.
 */
// function regexVar(s) {
//   /*
//    * Declare a RegExp object variable named 're'
//    * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
//    */
//   console.log(s);
//   // let re = new RegExp("^([aeiou])[a-z]*\\1$");
//   let re = /^([aeiou]).*\1$/;
//   console.log(re.test(s));

//   /*
//    * Do not remove the return statement
//    */
//   return re;
// }
// console.log(regexVar("bcdb"));
// console.log(regexVar("a"));
// console.log(regexVar("aa"));
// console.log(regexVar("2"));
// console.log(regexVar("acda"));
// console.log(regexVar("acde"));

/**
 * Task

Complete the function in the editor below by returning a RegExp object, , that matches any string  satisfying both of the following conditions:

String  starts with the prefix Mr., Mrs., Ms., Dr., or Er.
The remainder of string  (i.e., the rest of the string after the prefix) consists of one or more upper and/or lowercase English alphabetic letters (i.e., [a-z] and [A-Z]).
Constraints

The length of string  is  .
Output Format

The function must return a RegExp object that matches any string  satisfying both of the given conditions.

Sample Input 0
Mr.X - true

Sample Input 1
Mrs.Y - true

Sample Input 2
Dr#Joseph - false

Sample Input 3
Er .Abc - false
 */
// function regexVar(s) {
//   /*
//    * Declare a RegExp object variable named 're'
//    * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.',
//    * followed by one or more letters.
//    */
//   const re = /^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$/;
//   console.log(s);
//   console.log(re.test(s));

//   /*
//    * Do not remove the return statement
//    */
//   return re;
// }
// console.log(regexVar("Mr.X")); // true
// console.log(regexVar("Er.Ana")); // true
// console.log(regexVar("Ms.karen")); // true
// console.log(regexVar("Ms .Amanda")); // false
// console.log(regexVar("Ms#Amanda")); // false
// console.log(regexVar("Ms.12")); // false
// console.log(regexVar("Mr..jairo")); // false
// console.log(regexVar("Mr.Jairo.")); // false

/**
 * Task

Complete the function in the editor below by returning a RegExp object, , that matches every integer in some string .

Constraints

The length of string  is  .
It's guaranteed that string  contains at least one integer.
Output Format

The function must return a RegExp object that matches every integer in some string .

Sample Input 0

102, 1948948 and 1.3 and 4.5
Sample Output 0

102
1948948
1
3
4
5
Explanation 0

When we call match on string  and pass the correct RegExp as our argument, it returns the following array of results: [ '102', '1948948', '1', '3', '4', '5' ].
 */
// function regexVar(s) {
//   // const re = /^([0-9]+)\.?([0-9]*)$/;
//   // const re = /([0-9]+)/g;
//   const re = /(\d+)/g;

//   // console.log("re", re);
//   console.log("match", s.match(re));

//   return re;
// }
// console.log(regexVar("102, 1948948 and 1.3 and 4.5"));
// console.log(regexVar([1, 2, 3]));
