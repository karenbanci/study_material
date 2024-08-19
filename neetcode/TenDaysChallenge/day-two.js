/**
 * Task

Complete the getGrade(score) function in the editor. It has one parameter: an integer, , denoting the number of points Julia earned on an exam. It must return the letter corresponding to her  according to the following rules:

If 25 < score  <= 30 then grade = A
If 20 < score  <= 25 then grade = B
If 15 < score  <= 20 then grade = C
If 10 < score <= 15  then grade = D
If 5 < score   <= 10 then grade = E
If 0 < score  <= 5  then grade = F
Input Format

Stub code in the editor reads a single integer denoting  from stdin and passes it to the function.

Constraints

Output Format

The function must return the value of  (i.e., the letter grade) that Julia earned on the exam.

Sample Input 0

11
Sample Output 0

D
 */
// function getGrade(score) {
//   let grade;
//   // Write your code here
//   if (score > 25 && score <= 30) {
//     grade = "A";
//   } else if (score > 20 && score <= 25) {
//     grade = "B";
//   } else if (score > 15 && score <= 20) {
//     grade = "C";
//   } else if (score > 10 && score <= 15) {
//     grade = "D";
//   } else if (score > 5 && score <= 10) {
//     grade = "E";
//   } else {
//     grade = "F";
//   }

//   return grade;
// }
// console.log(getGrade(29));

// console.log(getGrade(25));
// console.log(getGrade(20));
// console.log(getGrade(15));
// console.log(getGrade(10));
// console.log(getGrade(5));
// console.log(getGrade(0));

/**
 *
 * Task

Complete the getLetter(s) function in the editor. It has one parameter: a string, , consisting of lowercase English alphabetic letters (i.e., a through z). It must return A, B, C, or D depending on the following criteria:

If the first character in string  is in the set {a,e,i,o,u}, then return A.
If the first character in string  is in the set {b,c,d,f,g}, then return B.
If the first character in string  is in the set {h,j,k,l,m}, then return C.
If the first character in string  is in the set {n,p,q,r,s,t,v,w,x,y,z}, then return D.
Hint: You can get the letter at some index  in  using the syntax s[i] or s.charAt(i).

Function Description

Complete the getLetter function in the editor below.

getLetter has the following parameters:

string s: a string
Returns

string: a single letter determined as described above
Input Format

Stub code in the editor reads a single string denoting  from stdin.

Constraints

, where  is the length of .
String  contains lowercase English alphabetic letters (i.e., a through z) only.
Sample Input 0

adfgt
Sample Output 0

A
 */

// function getLetter(s) {
//   let letter;
//   // Write your code here

//   const i = 0;
//   switch (true) {
//     case new Set(["a", "e", "i", "o", "u"]).has(s.charAt(i)):
//       letter = "A";
//       break;
//     case new Set(["b", "c", "d", "f", "g"]).has(s.charAt(i)):
//       letter = "B";
//       break;
//     case new Set(["h", "j", "k", "l", "m"]).has(s.charAt(i)):
//       letter = "C";
//       break;
//     default:
//       letter = "D";
//   }

//   return letter;
// }
// console.log(getLetter("adfgt"));
// console.log(getLetter("zdfgt"));
// console.log(getLetter("sdfgt"));
// console.log(getLetter("gdfgt"));

/**
 * Task

First, print each vowel in  on a new line. The English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in .
Second, print each consonant (i.e., non-vowel) in  on a new line in the same order as it appeared in .
Function Description

Complete the vowelsAndConsonants function in the editor below.

vowelsAndConsonants has the following parameters:

string s: the string to process
Prints

Print each vowel of  in order on a new line, then print each consonant in order on a new line. Return nothing.
Input Format

There is one line of input with the string .

Output Format

First, print each vowel in  on a new line (in the same order as they appeared in ). Second, print each consonant (i.e., non-vowel) in  on a new line (in the same order as they appeared in ).

Sample Input 0

javascriptloops
Sample Output 0

a
a
i
o
o
j
v
s
c
r
p
t
l
p
s

 */
// function vowelsAndConsonants(s) {
//   const vowels = new Set(["a", "e", "i", "o", "u"]);
//   const consoant = [];

//   for (let i = 0; i < s.length; i++) {
//     if (vowels.has(s[i])) {
//       console.log(s[i]);
//     } else {
//       consoant.push(s[i]);
//     }
//   }

//   for (let i = 0; i < consoant.length; i++) {
//     console.log(consoant[i]);
//   }
// }
// console.log(vowelsAndConsonants("javascriptloops"));
