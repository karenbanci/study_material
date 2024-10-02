const fs = require("fs");

// Read the file entrada.txt
const input = fs.readFileSync("bolsa-de-valores.txt", "utf8");
const lines = input.split("\n").map((texto) => texto.trim());

var contador = 0;
function getLine() {
  return lines[contador++];
}

let diasETaxa = getLine()
  .split(" ")
  .map((num) => parseInt(num));

let quantidadeDias = diasETaxa.slice(0, 1);
let taxa = diasETaxa.slice(1);

console.log(quantidadeDias, taxa);

let cotacoes = getLine()
  .split(" ")
  .map((num) => parseInt(num));

// console.log(cotacoes);

while (quantidadeDias != 0) {
  let diaCompra;
  let diaVenda;
  let arrMaxLucro = [];
  let maxLucro = 0;

  for (let i = 0; i < cotacoes.length - 1; i++) {
    for (let j = i + 1; j < cotacoes.length; j++) {
      // console.log(`dia: ${i} cotação: ${cotacoes[i]}`);
      diaCompra = Number(cotacoes[i]) + Number(taxa);
      diaVenda = Number(cotacoes[j]);
      console.log(`compra:${diaCompra} venda:${diaVenda}`);
      if (diaCompra > diaVenda) {
        continue;
      }
      arrMaxLucro.push(diaVenda - diaCompra);
      console.log("array de lucro", arrMaxLucro);
    }
    quantidadeDias--;
  }

  maxLucro = Math.max(...arrMaxLucro);
  console.log(maxLucro, "\n\n");
  return maxLucro;
}
// resposta no Beecrowd - Time limit exceeded
