// - Escreva uma função que receba um array de números e use o método `map` para retornar um novo array onde cada número seja multiplicado por 2.
// const numbers = [1, 2, 3, 4];
// const result = numbers.map((num) => {
//   return num * 2;
// });
// console.log(numbers, result);

// const multiply = (num) => num * 2;
// const resultTwo = numbers.map(multiply);
// console.log(resultTwo);

// - Crie uma função que receba um array de números e use o método `filter` para retornar um novo array contendo apenas os números maiores que 10.
// const arrNum = [2, 4, 6, 12, 15, 16, 3, 23, 5, 100];
// const filtered = arrNum.filter((num) => {
//   return num > 10;
// });
// console.log(filtered);

// - Escreva uma função que use o método `reduce` para calcular a soma de todos os elementos de um array.
// const arrNum = [2, 4, 6, 8, 100];
// const initialValue = 0;
// const sum = arrNum.reduce(
//   (accumulator, initialValue) => accumulator + initialValue,
//   initialValue
// );
// console.log(sum);

// - Crie uma função que use o método `find` para localizar o primeiro número par em um array.
// const arrNum = [1, 3, 5, 20, 23, 32, 55, 67, 89, 100];

// const findPeer = (arr) => {
//   const result = arr.find((num) => num % 2 === 0);
//   return result;
// };
// console.log(findPeer(arrNum));

// - Escreva uma função que use o método `every` para verificar se todos os números em um array são positivos.
// const arrNum = [1, 3, 5, 20, 23, 32, 55, 67, 89, 100];
// const arrNumTwo = [-1, -23, -4, 23, 1, 0, 2, -100, 100];

// const positiveNumber = (num) => {
//   return num > 0;
// };

// console.log(arrNum.every(positiveNumber));
// console.log(arrNumTwo.every(positiveNumber));

// - Crie uma função que use o método `some` para verificar se algum número em um array é maior que 20.
// const arrNum = [1, 3, 5, 20, 23, 32, 55, 67, 89, 100];
// const arrNumTwo = [1, 3, 5, 9, 19];

// const check = (arrNum) => {
//   return arrNum.some((num) => num > 20);
// };
// console.log(check(arrNum));
// console.log(check(arrNumTwo));

// - Escreva uma função que use o método `concat` para unir dois arrays de strings.
// const arr = ["Olá"];
// const arr2 = ["Mundo"];

// const joinArr = (arr) => {
//   return arr.concat(arr2);
// };
// console.log(joinArr(arr));

// - Crie uma função que use os métodos `shift` e `pop` para remover o primeiro e o último elemento de um array, respectivamente.
// const remove = (arr) => {
//   arr.shift();
//   arr.pop();
//   return arr;
// };
// const arr = ["a", "b", "c", "d", "e", "f", "g"];
// console.log(remove(arr));

// - Escreva uma função que use os métodos `unshift` e `push` para adicionar elementos no início e no final de um array, respectivamente.
// const add = (arr, inicio, fim) => {
//   arr.unshift(inicio);
//   arr.push(fim);
//   return arr;
// };
// const arr = ["a", "b", "c", "d", "e", "f", "g"];
// console.log(add(arr, "kaka", "jairo"));

// - Crie uma função que use o método `sort` para ordenar um array de números em ordem crescente.
// const organizar = (arr) => {
//   return arr.sort((a, b) => a - b);
// };
// const arrNum = [-1, -23, -4, 23, 1, 0, 2, -100, 100];
// const arrNumTwo = [2, 5, 3, 6, 1, 12];
// console.log(organizar(arrNum));
// console.log(organizar(arrNumTwo));

// - Escreva uma função que use o método `toUpperCase` para converter uma string em letras maiúsculas.
// const upper = (str) => {
//   return str.toUpperCase();
// };
// console.log(upper("hola mundo, como voce esta?"));

// - Crie uma função que use o método `toLowerCase` para converter uma string em letras minúsculas.
// const lower = (str) => {
//   return str.toLowerCase();
// };
// console.log(lower("QUERIA ESTAR DORMINDO"));

// - Escreva uma função que use o método `replace` para substituir todas as ocorrências de uma palavra em uma string por outra palavra.
// const substituir = (str, original, nova) => {
//   return str.replaceAll(original, nova);
// };
// console.log(
//   substituir(
//     "O rato comeu a roupa do rei de roma, comeu o rato",
//     "rato",
//     "cachorro"
//   )
// );

// - Crie uma função que use o método `substring` para extrair uma parte específica de uma string.
// const sub = (str, start, end) => {
//   return str.substring(start, end);
// };
// console.log(sub("O rato comeu a roupa do rei de roma, comeu o rato", 15, 20));

// - Escreva uma função que use o método `split` para dividir uma string em um array de palavras, com base nos espaços.
// const separar = (arr, ponto) => {
//   return arr.split(ponto);
// };
// console.log(separar("Queria comer bolo", " "));

// - Crie uma função que use o método `trim` para remover espaços em branco no início e no final de uma string.
// const remove = (str) => {
//   return str.trim();
// };
// console.log(remove(" Oi Mundo  "));

// - Escreva uma função que use o método `join` para juntar os elementos de um array em uma string, separados por vírgulas.
// const juntar = (arr) => {
//   return arr.join(",");
// };
// console.log(juntar(["Jairo", "eu", "te", "amo"]));

// - Crie uma função que use o método `startsWith` para verificar se uma string começa com uma sequência específica de caracteres.
// const comecar = (str, search) => {
//   return str.startsWith(search);
// };
// console.log(comecar("Jairo eu te amo", "Jairo"));

// - Escreva uma função que use o método `endsWith` para verificar se uma string termina com uma sequência específica de caracteres.
// const termina = (str, search) => {
//   return str.endsWith(search);
// };
// console.log(termina("Jairo eu te amo", "amo"));
// console.log(termina("Jairo eu te amo", "amor"));

// - Crie uma função que use o método `indexOf` para encontrar a posição de uma substring dentro de uma string.
// const index = (str, index) => {
//   return str.indexOf(index);
// };
// console.log(index("Jesus ama você", "ama"));

// - Dado um array de números, escreva uma função que retorne a soma de todos os elementos no array.
// const somar = (arr) => {
//   let init = 0;
//   for (let i = 0; i < arr.length; i++) {
//     // console.log(arr[i]);
//     init += arr[i];
//   }
//   return init;
// };
// console.log(somar([1, 2, 3, 4]));

// - Escreva uma função que receba um array de números e retorne um novo array apenas com os números pares.
// const pares = (arr) => {
//   let newArr = [];
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] % 2 === 0) {
//       newArr.push(arr[i]);
//     }
//   }
//   return newArr;
// };
// console.log(pares([3, 4, 5, 6, 7, 8, 9]));

// - Crie uma função que inverta a ordem dos elementos em um array sem usar o método `reverse`.
// const reverter = (arr) => {
//   let newArr = [];
//   let i = arr.length - 1;
//   while (i >= 0) {
//     newArr.push(arr[i]);
//     i--;
//   }
//   // for (let i = arr.length - 1; i >= 0; i--) {
//   //   newArr.push(arr[i]);
//   // }
//   return newArr;
// };
// console.log(reverter([2, 4, 6, 3, 8, 1, 9]));

// - Escreva uma função que receba um array de strings e retorne um novo array apenas com os nomes únicos (sem duplicados).
// const unicos = (arr) => {
//   let dic = {};
//   for (let i = 0; i < arr.length; i++) {
//     dic[arr[i]] = 1; // arr[i];
//     // console.log("dic", dic);
//   }
//   const newArr = Object.keys(dic);

//   return newArr;
// };
// console.log(unicos(["pao", "moeda", "Brazil", "pao"]));
// console.log(
//   unicos([
//     "pao",
//     "moeda",
//     "Brazil",
//     "Peru",
//     "moeda",
//     "Brazil",
//     "Peru",
//     "moeda",
//     "Brazil",
//     "Peru",
//     "moeda",
//     "Brazil",
//     "Peru",
//     "moeda",
//     "Brazil",
//     "Peru",
//   ])
// );

// - Dado um array de números, escreva uma função que retorne o produto de todos os elementos no array.
// const produto = (arr) => {
//   let result = 1;
//   for (let i = 0; i < arr.length; i++) {
//     result *= arr[i];
//   }
//   return result;
// };
// console.log(produto([3, 4, 5, 6]));

// - Escreva uma função que receba uma string e retorne a mesma string invertida.
// const revertida = (str) => {
//   str = str.split("").reverse().join("");
//   return str;
// };
// console.log(revertida("Jairo é lindo!"));

// - Crie uma função que receba uma string e retorne o número de vogais que ela contém.

// O(n^2)
// const vogais = (str) => {
//   let result = [];
//   const vowel = {
//     a: "a",
//     e: "e",
//     i: "i",
//     o: "o",
//     u: "u",
//   };
//   const vog = Object.values(vowel);
//   const arr = str.split("");

//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < vog.length; j++) {
//       if (arr[i] === vog[j]) {
//         result.push(arr[i]);
//       }
//     }
//   }
//   return result;
// };
// console.log(vogais("Javascript"));
// O(n);
// const vogais = (str) => {
//   let result = [];
//   const vowel = {
//     a: "a",
//     e: "e",
//     i: "i",
//     o: "o",
//     u: "u",
//   };
//   // const vog = Object.values(vowel);
//   const arr = str.split("");

//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] in vowel) {
//       result.push(arr[i]);
//     }
//   }
//   return result;
// };
// console.log(vogais("Javascript"));

//- Escreva uma função que determine se uma string dada é um palíndromo (lê-se igual de frente para trás).
// const palindromo = (str) => {
//   const lower = str.toLowerCase();
//   let inicio = 0;
//   let fim = lower.length - 1;

//   while (inicio < fim) {
//     // console.log("inicio:", inicio, "->", lower[inicio]);
//     // console.log("fim:", fim, "->", lower[fim]);

//     if (lower[inicio] !== lower[fim]) {
//       return false;
//     }
//     inicio++;
//     fim--;
//   }
//   return true;
// };
// console.log(palindromo("Ana"));
// console.log(palindromo("Anna"));
// console.log(palindromo("Caminhao"));
// console.log(palindromo("Abca"));

// - Crie uma função que substitua todos os espaços em uma string por underscores (`_`).
// const substituir = (str) => {
//   return str.replaceAll(" ", "_");
// };
// console.log(
//   substituir(
//     "Crie uma função que substitua todos os espaços em uma string por underscores"
//   )
// );

// - Escreva uma função que receba uma string e retorne a substring mais longa sem caracteres repetidos.
// const substring = (str) => {
//   const mapaCaracteres = new Map();
//   let inicio = 0;
//   // let maxComprimento = 0;

//   for (let fim = 0; fim < str.length; fim++) {
//     const char = str[fim];

//     // Se o caractere já foi visto e está dentro da janela atual, mova o início da janela
//     if (mapaCaracteres.has(char) && mapaCaracteres.get(char) >= inicio) {
//       inicio = mapaCaracteres.get(char) + 1;
//     }

//     // Atualiza ou adiciona o índice do caractere no mapa
//     mapaCaracteres.set(char, fim);
//     console.log(mapaCaracteres);

//     // Calcula o comprimento da janela atual
//     // maxComprimento = Math.max(maxComprimento, fim - inicio + 1);
//   }
//   // console.log(mapaCaracteres);

//   const subStr = [...mapaCaracteres.keys()].join("");
//   console.log("substring =>", subStr);

//   return subStr;
// };
// console.log(substring("calculadora"));
// console.log(substring("tomate"));
// console.log(substring("anna"));

// function substringMaisLongaSemRepetidos(s) {
//   const mapaCaracteres = new Map();
//   let inicio = 0;
//   let maxComprimento = 0;
//   let inicioMax = 0;

//   for (let fim = 0; fim < s.length; fim++) {
//     const char = s[fim];

//     // Se o caractere já foi visto e está dentro da janela atual, mova o início da janela
//     if (mapaCaracteres.has(char) && mapaCaracteres.get(char) >= inicio) {
//       inicio = mapaCaracteres.get(char) + 1;
//     }

//     // Atualiza ou adiciona o índice do caractere no mapa
//     mapaCaracteres.set(char, fim);

//     // Verificamos se o comprimento da janela atual é maior que o comprimento máximo encontrado
//     if (fim - inicio + 1 > maxComprimento) {
//       maxComprimento = fim - inicio + 1;
//       inicioMax = inicio;
//     }
//   }

//   // Retorna a substring mais longa encontrada
//   return s.slice(inicioMax, inicioMax + maxComprimento);
// }

// // Exemplo de uso
// const input = "calculadora";
// const output = substringMaisLongaSemRepetidos(input);

// console.log(output); // "lculador"

// - Escreva uma função que receba um array e um valor, e retorne o primeiro índice em que o valor é encontrado. Se não for encontrado, retorne `-1`.
// const encontre = (arr, val) => {
//   for (let i = 0; i < arr.length; i++) {
//     console.log("arr[i]", arr[i], "index", i);
//     // console.log("val", val);
//     if (val === arr[i]) {
//       return i;
//     }
//   }
//   return -1;
// };
// console.log(encontre([1, 2, 6, 4, 3, 8], 7));
// console.log(encontre([1, 2, 6, 4, 3, 23], 32));
// console.log(encontre([1, 2, 6, 73, 3, 23], 73));
// console.log(encontre([1, 2, 6, 4, 3, 8], 6));

// - Dado um array de números, escreva uma função que mova todos os zeros para o final do array, mantendo a ordem dos outros elementos.
// const ordem = (arr) => {
//   let newArr = [];
//   let count = 0;
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] !== 0) {
//       // arr[i].remove();
//       newArr.push(arr[i]);
//     } else {
//       count++;
//     }
//   }
//   for (let j = 0; j < count; j++) {
//     newArr.push(0);
//   }

//   // console.log(newArr);
//   return newArr;
// };
// console.log(ordem([0, 2, 5, 200, 0, 70, 27]));

//A. Faz uma funcao que recebe um string, e devolve o string invertido. Só pode usar um for assim: for (i=0;i<len;i++){...}
// const revert = (str) => {
//   let output = "";

//   for (let i = 0; i < str.length; i++) {
//     let calculator = str.length - i - 1;
//     output += str[calculator];

//     console.log(calculator);
//   }
//   return output;
// };
// console.log(revert("COMPUTADOR"));

/* B. Faz uma funcao que recebe um string, e printa cada letra de tras pra frente, e de frente pra tras. Só pode usar um (só um) FOR assim: for (i=0;i<len;i++){...}

Exemplo: Jairo
Jo
ar
ii
ra
oJ
*/
// const parInvertido = (str) => {
//   for (let i = 0; i < str.length; i++) {
//     let calculator = str.length - i - 1;
//     // console.log(calculator);
//     console.log(str[i], str[calculator]);
//   }
// };
// console.log(parInvertido("JAIRO"));

// - Escreva uma função que receba um array de números e retorne todos os pares de números que somem a um valor dado.
// const pares = (arr, target) => {
//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < i; j++) {
//       let calculo = target - arr[i] - arr[j];
//       // console.log(calculo);
//       if (calculo === 0 && arr[i] !== arr[j]) {
//         let newArr = [arr[i], arr[j]];
//         console.log(newArr);
//       }
//     }
//   }
// };
// console.log(pares([2, 3, 5, 8, 4, 6, 10, 9, 1, 0], 10));

// - Dado um array, escreva uma função que o rotacione `k` posições para a direita.
// const mudarPosicao = (arr, k, target) => {
//   const index = k;

//   for (let i = 0; i < arr.length; i++) {
//     // console.log(arr[i - k]);
//     if (arr[i] === target) {
//       // console.log(arr[i]);
//       const temp = arr[index];
//       console.log("temporario", temp);
//       arr[index] = arr[i];
//       arr[i] = temp;
//       console.log(arr);
//     }
//     // const newArr =
//   }
// };
// //                        0     1    2    3   4
// console.log(mudarPosicao(["K", "A", "R", "E", "N"], 2, "K"));
// // output                 "A", "R", "K", "E", "N"

// - Crie uma função que receba um array e dois índices, e troque os elementos nessas posições.
// const changePosition = (arr, first, second) => {
//   let indexTemp = arr[first];
//   arr[first] = arr[second];
//   arr[second] = indexTemp;

//   return arr;
// };
// console.log(changePosition([2, 3, 4, 5], 0, 3));
// console.log(changePosition(["Jairo", "Karen", "Patricia", "Liamara"], 1, 3));

/** Encontrar dois números em uma lista que somam a um valor-alvo dado e retornar seus índices. */
// const findIndex = (list, target) => {
//   for (let i = 0; i < list.length; i++) {
//     for (let j = 0; j < list.length; j++) {
//       if (list[i] + list[j] === target) {
//         console.log("result", i, j);
//         return [i, j];
//       }
//     }
//   }
// };
// console.log(findIndex([1, 2, 3, 4, 5], 4)); // 0,2

/* Verificar se um número inteiro é um palíndromo, ou seja, se ele é igual quando lido de trás para frente. */
// const palindromo = (int) => {
//   const arr = int.toString().split("");
//   let inicio = 0;
//   let fim = arr.length - 1;

//   while (inicio < fim) {
//     if (arr[inicio] !== arr[fim]) {
//       console.log(inicio, fim);
//       return false;
//     }
//     inicio++;
//     fim--;
//   }
//   return true;
// };
// console.log(palindromo(2012));
// console.log(palindromo(2002));

/* Converter um número representado em algarismos romanos para um número inteiro. */
// const convert = (str) => {
//   const arr = str.split("");
//   let result = 0;

//   const romanMap = {
//     I: 1,
//     V: 5,
//     X: 10,
//     L: 50,
//     C: 100,
//     D: 500,
//     M: 1000,
//   };

//   for (let i = 0; i < arr.length; i++) {
//     const current = romanMap[arr[i]];
//     console.log("current", current);
//     const next = romanMap[arr[i + 1]];
//     console.log("next", next);

//     if (next && current < next) {
//       result -= current;
//     } else {
//       result += current;
//     }
//   }

//   return result;
// };
// // console.log(convert("XXI"));
// console.log(convert("XIV"));

// FIZZBUZZ
// function fizzBuzz(n) {
//   // console.log(n);
//   // Write your code here
//   for (let i = 1; i <= n; i++) {
//     if (i % 3 === 0 && i % 5 === 0) {
//       console.log("FizzBuzz");
//     } else if (i % 3 === 0) {
//       console.log("Fizz");
//     } else if (i % 5 === 0) {
//       console.log("Buzz");
//     } else {
//       console.log(i);
//     }
//   }
// }
// console.log(fizzBuzz(15));

// // Max difference
// const maxDifference = (px) => {
//   let max = 0;
//   let foundPositiveDiff = false;

//   for (let i = 0; i < px.length; i++) {
//     for (let j = i + 1; j < px.length; j++) {
//       console.log("i", px[i], "j", px[j]);
//       if (px[i] < px[j]) {
//         let curr = px[j] - px[i];
//         console.log("px[j] - px[i]", curr);
//         foundPositiveDiff = true; // Indica que encontramos uma diferença positiva

//         if (curr > max) {
//           max = curr;
//         }
//       }
//     }
//   }

//   if (!foundPositiveDiff) {
//     return -1; // Retorna -1 se nenhuma diferença positiva foi encontrada
//   }

//   return max;
// };

// console.log(maxDifference([7, 1, 2, 5])); // 4

/** Verificar se todos os parênteses em uma string estão corretamente balanceados e fechados. */
// const parenteses = (str) => {
//   let stack = [];

//   for (let i = 0; i < str.length; i++) {
//     if (str[i] === "(") {
//       stack.push(str[i]);
//     } else if (str[i] === ")") {
//       // Se encontramos um parêntese de fechamento sem ter um de abertura correspondente
//       if (stack.length === 0) {
//         return false;
//       }
//       stack.pop();
//     }
//   }

//   // Se a pilha estiver vazia no final, os parênteses estão balanceados
//   return stack.length === 0;
// };

// console.log(parenteses("()"));
// console.log(parenteses("(()"));
// console.log(parenteses("(())"));
// console.log(parenteses("(()))"));

/**Fundir duas listas encadeadas que estão ordenadas em uma única lista ordenada. */
// class Node {
//   constructor(data) {
//     (this.data = data), (this.next = null);
//   }
// }

// class LinkedList {
//   constructor(head) {
//     this.head = null; // sempre inicializa com null
//   }

//   append(data) {
//     const newNode = new Node(data);

//     // se a cabeça for nula
//     if (this.head === null) {
//       //o dado vai ser colocado na cabeça
//       this.head = newNode;
//       return;
//     }

//     // Adicionar no último node
//     // atual node é a cabeça
//     let current = this.head;

//     //enquanto o próximo do atual for diferente de nulo
//     while (current.next !== null) {
//       // atual será atual do proxmo
//       current = current.next;
//     }

//     // o próximo é o dado - adicionar o dado no último node
//     current.next = newNode;
//   }

//   printList() {
//     let current = this.head;
//     let listStr = "";
//     while (current !== null) {
//       listStr += current.data + "->";
//       current = current.next;
//     }
//     console.log(listStr + "null");
//   }

//   remove(data) {
//     if (this.head === null) {
//       return;
//     }

//     if (this.head.data === data) {
//       this.head = this.head.next;
//       return;
//     }

//     let current = this.head;
//     let prev = null;

//     // buscar o nó a ser removido
//     while (current !== null && current.data !== data) {
//       prev = current;
//       current = current.next;
//     }

//     // se nao tiver na lista
//     if (current === null) {
//       return;
//     }

//     prev.next = current.next;
//   }
// }

// const linkedListOne = new LinkedList();

// // Adicionando elementos
// linkedListOne.append(5);
// linkedListOne.append(6);
// linkedListOne.append(9);

// // Imprimindo a lista
// console.log("Lista original One:");
// linkedListOne.printList();

// const linkedListTwo = new LinkedList();

// // Adicionando elementos
// linkedListTwo.append(7);
// linkedListTwo.append(10);
// linkedListTwo.append(18);

// // Imprimindo a lista
// console.log("Lista original Two:");
// linkedListTwo.printList();

// const joinLinkedList = (listOne, listTwo) => {
//   console.log(listOne.head);
//   console.log(listTwo.head);

//   // Achar o ultimo node do primeiro LL
//   let current = listOne.head;

//   // --- enquanto o proximo do atual != de nulo
//   while (current.next != null) {
//     // atual será atual do proximo
//     current = current.next;
//   }
//   console.log("atual", current);

//   // Adicionar a head do segundo LL ao último node do primeiro LL
//   let head = listTwo.head;
//   current.next = head;

//   // retorna a primeira LL
//   console.log("ver se deu certo", listOne);
//   //]]-
//   listOne.printList();
// };
// console.log(joinLinkedList(linkedListOne, linkedListTwo));

/**
Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"

array
index    0  1  2
         x  y  z

string
index    0   1   2   3   4   5   6   7
         x   y   y   z   y   z   y   x

output -> zyx

// a substring só é válida se tiver todos os caracteres da array
 */

// function getShortestUniqueSubstring(arr, str) {
//   const charMap = new Map();
//   let left = 0;
//   let minLength = Infinity;
//   let minSubstring = "";
//   let uniqueCounter = 0;

//   // Inicializa o mapa de caracteres
//   for (const char of arr) {
//     charMap.set(char, 0);
//   }
//   console.log("charMap", charMap);
//   // Expande a janela deslizante com o ponteiro direito (right)
//   for (let right = 0; right < str.length; right++) {
//     const rightChar = str[right];

//     if (charMap.has(rightChar)) {
//       if (charMap.get(rightChar) === 0) {
//         uniqueCounter += 1;
//       }
//       charMap.set(rightChar, charMap.get(rightChar) + 1);
//     }

//     // Contrai a janela deslizante com o ponteiro esquerdo (left)
//     while (uniqueCounter === arr.length) {
//       const currentLength = right - left + 1;

//       if (currentLength < minLength) {
//         minLength = currentLength;
//         minSubstring = str.substring(left, right + 1);
//       }

//       const leftChar = str[left];
//       if (charMap.has(leftChar)) {
//         if (charMap.get(leftChar) === 1) {
//           uniqueCounter -= 1;
//         }
//         charMap.set(leftChar, charMap.get(leftChar) - 1);
//       }

//       left += 1;
//     }
//   }

//   return minSubstring;
// }

// console.log(getShortestUniqueSubstring(["x", "y", "z"], "xyyzyzyx"));
