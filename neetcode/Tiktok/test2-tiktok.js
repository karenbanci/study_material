/* retornar o numero maximo de categorias que dois usuários tem em comum
o input é uma array e cada elemento representa numero de categorias

input=[4,2,6,8]
output = 4

input=[3,2,5]
output = 4

input=[4,8,2,16]
output = 8

*/

function maxCommonCategories(input) {
  // Inicialmente, o número máximo de categorias em comum é 0
  let maxCategories = 0;

  // Para cada par de categorias no input
  for (let i = 0; i < input.length; i++) {
    for (let j = i + 1; j < input.length; j++) {
      // Calcula o máximo divisor comum (GCD) entre dois números
      let commonCategories = gcd(input[i], input[j]);
      // Atualiza o número máximo de categorias em comum, se necessário
      if (commonCategories > maxCategories) {
        maxCategories = commonCategories;
      }
    }
  }

  return maxCategories;
}

// Função auxiliar para calcular o máximo divisor comum (GCD) usando o algoritmo de Euclides
function gcd(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

// Testes
console.log(maxCommonCategories([4, 2, 6, 8])); // Output: 4
console.log(maxCommonCategories([3, 2, 5])); // Output: 1
console.log(maxCommonCategories([4, 8, 2, 16])); // Output: 8
