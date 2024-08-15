/*
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

example:
input = "Mr John Smith    ", 13
output = "Mr%20John%20Smith"
*/

var urlify = function (str, length) {
  // have a pointer to check from start to end
  var strArr = str.split("");
  console.log(strArr);
  var pointer = 0;

  console.log(strArr[pointer]);
  while (pointer < str.length) {
    if (strArr[pointer] === " ") {
      // *** needs more work here, a little wierd
      // not handling trailing spaces properly
      for (let i = 0; strArr.length; i++) {
        console.log("strArr[i]", strArr[i]);
      }
      // strArr[pointer] = "%";
      // strArr[pointer + 1] = "2";
      // strArr[pointer + 2] = "0";
      // console.log(strArr, strArr.length);
    }
    pointer++;
  }
  // if character is a space, move remainder chars by two
  // replace following three chars with '%20'
  // return strArr.join("");
};

console.log(urlify("Mr John Smith    ", 13));
