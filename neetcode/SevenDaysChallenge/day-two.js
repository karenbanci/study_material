/**
 * Given an array of integers, where all elements but one occur twice, find the unique element.

Example = [1,2,3,4,3,2,1]

The unique element is 4.
 */
function lonelyinteger(a) {
  // Write your code here
  // colocar em um set e separar quem estiver duplicado

  const arrSet = new Set();
  const duplicate = new Set();

  for (let num of a) {
    if (arrSet.has(num)) {
      duplicate.add(num);
    } else {
      arrSet.add(num);
    }
  }
  console.log(arrSet, duplicate);

  duplicate.forEach((element) => arrSet.delete(element));
  console.log(arrSet, duplicate);

  let unique = "";

  for (let i = a.length - 1; i >= 0; i--) {
    if (arrSet.has(a[i])) {
      unique = a[i];
      break;
    }
  }
  console.log(unique);
  return unique;
}
lonelyinteger([1, 2, 3, 4, 3, 2, 1]);
