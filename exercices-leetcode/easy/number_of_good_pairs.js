/*
terei que retornar numeros que formam parzinhos

index   0 1 2 3 4 5
nums = [1,2,3,1,1,3]

primeiro passo
iteirar cada elemento da array, preciso ter 2 elementos pra comprarar
for (let i = 0; i < nums.length; i++)
for (let j = 0; j < nums.length; j++)

pares index - esse vai ser o resultado
0,3
0,4
3,4
2,5
total 4 pares

*/

var numIdenticalPairs = function (nums) {
  let numPairs = 0;
  for (let i = 0; i < nums.length; i++) {
    // j = i + 1 -> para ele fazer a leitura indo para a direçao direita da array
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] == nums[j]) {
        // aqui ele armazena numero de pares, ou seja, ele vai ver quantos conjuntos (i,j) e armazenar o numero de conjuntos
        numPairs++

        // console.log(`index dos pares ${totalPairs}`)
      }
    }
  }
  // O novo valor da propriedade length do objeto no qual o método foi chamado.
  console.log(`total de pares ${numPairs}`);
  return numPairs
};
const nums = [1, 2, 3, 1, 1, 3];
console.log(numIdenticalPairs(nums));
