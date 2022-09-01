/*
Given two strings, write a method to decide if one is a permutation of the other
pg.90
*/

function permutation(a, b) {

  const sortA = a.split("").sort().join("");
  const sortB = b.split("").sort().join("");

  console.log("array A: " + sortA);
  console.log("array B: " + sortB);

 if(sortA == sortB) {
  return true;
 } else {
  return false
 }

}


const a = "casaco";
const b = "sacoca";

console.log(permutation(a, b));


