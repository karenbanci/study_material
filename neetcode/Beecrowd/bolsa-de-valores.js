const fs = require("fs");

// Read the file entrada.txt
const input = fs.readFileSync("bolsa-de-valores.txt", "utf8");
const lines = input.split("\n").map((texto) => texto.trim());

var contador = 0;
function getLine() {
  return lines[contador++];
}

// Ler a primeira linha (N = quantidade de dias, C = taxa)
let [quantidadeDias, taxa] = getLine()
  .split(" ")
  .map((num) => parseInt(num));

// Ler a segunda linha (as cotações diárias)
let cotacoes = getLine()
  .split(" ")
  .map((num) => parseInt(num));

function maxLucro(quantidadeDias, taxa, cotacoes) {
  // Inicializar o menor preço como o primeiro dia
  let menorPreco = cotacoes[0];
  let maxLucro = 0; // O lucro máximo começa como zero

  // Iterar pelas cotações a partir do segundo dia
  for (let i = 1; i < quantidadeDias; i++) {
    // Calcular o lucro se vendermos no dia i
    let lucro = cotacoes[i] - menorPreco - taxa;

    // Atualizar o lucro máximo se o atual for maior
    if (lucro > maxLucro) {
      maxLucro = lucro;
    }

    // Atualizar o menor preço de compra se o preço atual for menor
    if (cotacoes[i] < menorPreco) {
      menorPreco = cotacoes[i];
    }
  }

  // Se não houver lucro positivo, o investidor não compra
  return maxLucro > 0 ? maxLucro : 0;
}

// Executar o cálculo do lucro máximo
const resultado = maxLucro(quantidadeDias, taxa, cotacoes);
console.log(resultado);
