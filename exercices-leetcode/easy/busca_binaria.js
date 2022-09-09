// link do challenge: https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array

const primarios = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

let target = 89;

// valor de retorno da função será o índice da posição onde o valor alvo foi encontrado
let chute = '';

// o código deve aceitar uma entrada
// deve retornar uma saída
// deve aceitar diferentes entradas

// 1-- Defina min = 0 e max = n-1.
// 2-- Se max < min, então pare: o alvo não está presente no array. Retorne -1.
// 3-- Calcule o chute como sendo a média entre max e min, arredondando para baixo (então será um número inteiro).
// 4-- Se array[chute] for igual ao alvo, então pare. Você o encontrou! Retorne chute.
// 5-- Se o chute foi muito baixo, ou seja, array[chute] < alvo, então defina min = guess + 1.
// 6-- Caso contrário, o chute foi muito alto. Defina max = guess - 1.
// 7-- Volte para o passo 2.

// Ele deve ser um loop for ou um loop while? Se você realmente quisesse usar um loop for, poderia fazê-lo, mas os índices supostos pela busca binária não estão na ordem sequencial que o loop for torna-se inconveniente. Primeiro, podemos selecionar o índice 12, então o 18, com base em algumas computações. Então, um loop while é a melhor opção.


let binarySearch = (primarios, target) => {
  let indiceMin = 0;
  let indiceMax = primarios.length - 1;

  // let indiceMin = function(){
  //   for (let i = 0; i < primarios.length; i++){
  //     console.log(primarios[i])
  //   }
  // }
  // let indiceMax = function() {
  //   for (let j = 0; j > primarios.length; i--) {
  //     return n - 1
  //   }
  // }

    // console.log(indiceMin, indiceMax);
    // console.log(Math.round((indiceMin + indiceMax) / 2));


  while (true){
    chute = Math.round((indiceMin + indiceMax)/2)
    console.log(indiceMin, indiceMax);
    console.log(chute);

    if (indiceMax < indiceMin) {
      console.log("o alvo nao esta na array")
      return -1
    }

    if (primarios[chute] === target ){
      console.log('Voce encontrou o numero');
      return chute;
    } else if (primarios[chute] < target) {
      indiceMin = chute + 1;
    } else if (primarios[chute] > target) {
      indiceMax = chute - 1;
    } else {
      console.log('te amoooooo')
    }
  }
  console.log('piiiiiiiiii')
  return -1;
}
let result = binarySearch(primarios, target)
console.log(`Encontou o index do número primario: ${result}`);
