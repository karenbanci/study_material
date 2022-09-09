const s = "abcde";
const arr = ["d", "a", "f", "g", "e"];
const cvs = "d,a,g,e,b";
// saida: ade

function on_the_hunt(s, arr, csv) {
  // Write your code here
  const string = s.split("");
  console.log('string', string);

  const cvsInArray = csv.split(",");
  console.log('CVS', cvsInArray);

  console.log('array', arr);
  let result = '';

  for(let i = 0; i < string.length; i++){
    for(let j = 0; j < arr.length; j++){
      for(let k = 0; k < cvsInArray.length; k++){
        if(string[i] === cvsInArray[k] && string[i] === arr[j]){
          result += string[i];
        }
      }
    }
  }
  return result;
  
}

console.log(on_the_hunt(s,arr,cvs));
