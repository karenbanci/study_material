// 1) O output é um array que contém cada elemento de a multiplication por cada elemento de b.

function multiplication(a, b) {
  const result = [];

  for(let i = 0; i < a.length; i++){
    for(let j = 0; j < b.length; j++){
      result.push(a[i]* b[j])
    }
  }
  return result;
}

const a = [1, 2, 3];
const b = [5, 6, 7];
console.log('resultado do primeiro exercício', multiplication(a, b));

console.log(" ------------ exercício 2 ---------------");

// 2) O output é uma array que contém cada elemento de a concatenado com cada elemento de 5 em formato de string
function concatenate(c, d) {
  const arrayToConcat = [];
  let string = "";
  // const stringC = c.toString().replace("," , "");
  // const stringD = d.toString().replace(",", "");


  for (let i = 0; i < c.length; i++) {
    for (let j = 0; j < d.length; j++) {
      // soma de string com numero resulta em string
      string += (c[i].toString() + d[j]);
    }
    arrayToConcat.push(string);
    string = '';
  }
  // console.log("resultado final: ", arrayToConcat);
  return arrayToConcat;
}

const c = [1, 2];
const d = [5, 6];
console.log("saída esperada: ['1516' , '2526']");
console.log(concatenate(c, d));
