//  ALGORITMO FIBONACCI -------------------------------------------
/*
let fibonacci = [];

fibonacci[0] = 0;
fibonacci[1] = 1;
fibonacci[2] = 1;

for (let i = 3; i < 30; i++) {
//index resultado = index index resultado -1 + index resultado -2
  fibonacci[i] = fibonacci[i -1] + fibonacci[i -2]
}

console.log(fibonacci);
*/

// ADICIONAR OU DELETAR ELEMENTOS DA ARRAY ----------------
/*
let numbers = [0,1,2,3,4,5,6,7,8,9];
// console.log(numbers.length);

// aqui está medindo a quantidade de infex que tem na array
// numbers[numbers.length] = 10;

// para adicionar elemento no final da array
numbers.push(10);
console.log(numbers.length);
console.log(numbers);


// para adicionar elemento no inicio da array
numbers.unshift(-1);
console.log(numbers.length);
console.log(numbers);

// para remover o último elemento da array e nao precisa de valor dentro dos parenteses
numbers.pop();
console.log(numbers.length);
console.log(numbers);

//  para remover o primeiro elemento da array nao precisa de valor dentro dos parenteses
numbers.shift();
console.log(numbers.length);
console.log(numbers);
 */

//  ADICIONAR E REMOVER ELEMENTOS NUMA POSIÇÃO ESPECÍFICA ------------------------------------------------------
/*
let numbers = [0,1,2,3,4,5,6,7,8,9];

// remover - vou remover elementos a partir da posição index 3 e 3 elementos seguintes (3,4,5)
numbers.splice(3,3);
console.log(numbers);

// adicionar - adicionar a partir do index 3, o segundo valor depois da vírgula é se eu fosse remover um elemento, mas vou remover 0 elementos. 3,4 e 5 são os valores a serem adicionados a partir do index 3
numbers.splice(3, 0, 30,40,50);
console.log(numbers);
*/

// ARRAYS BIDIMENSIONAIS
/*
let avgTempWeek = [];

let avgTempWeek1 = [19, 18, 21, 23.5, 24, 22.9, 27];
let avgTempWeek2 = [31, 33, 32.5, 34, 32, 31.4, 29];

// criei 2 arrays, para eu juntar em uma array só
// ou seja, na posição index 0 to add array 1 e na posição index 1 to add array 2
avgTempWeek[0] = avgTempWeek1;
avgTempWeek[1] = avgTempWeek2;

console.log(avgTempWeek)

// para eu acessar um elemento especifico da array avgTempWeek
console.log(avgTempWeek[0][4]) // 24
*/

// ARRAY MULTIDIMENSIONAL
/*
let month = [];

let firstWeeks =[];
let lastWeeks =[];

let avgTempWeek1 = [19, 18, 21, 23.5, 24, 22.9, 27];
let avgTempWeek2 = [31, 33, 32.5, 34, 32, 31.4, 29];


let avgTempWeek3 = [14, 13, 21, 20.5, 19, 21.9, 19.5];
let avgTempWeek4 = [20, 21, 22.2, 19.2, 17, 16.4, 17.8];

firstWeeks = [avgTempWeek1, avgTempWeek2];
lastWeeks = [avgTempWeek3, avgTempWeek4];

month = [firstWeeks, lastWeeks];
console.log(month[1][1][4]);

// iterar a cada elemento do mês (month)
for (let i = 0; i < month.length; i++){
  for (let j = 0; j < month.length; j++){
    for (let k = 0; k < month[i][j].length; k++){
      console.log(month[i][j][k]);
    }
  }
}
*/
