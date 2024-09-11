/**
 * beecrowd 2296
 *
 * Quantificar o desnível em uma direção?
 * desnível = soma das diferenças
 *
 * Planejamento:
 * 1) Coleta dos dados
 * 2) Calcular o desnível de cada trilha
 * 3) Comparar as trilhas, retornar a trilha menor
 *
 * Pseudocódigo
 * Para cada ponto da trilha
 *  subida, descida = 0, 0
 *
 * Se o ponto_atual < próximo_ponto:
 *    subida = próximo_ponto - ponto_atual
 * Se ponto_atual > próximo_ponto:
 *    descida = ponto_atual - próximo_ponto
 *
 * Trilha.i.esforço = min(subida, descida)
 *
 * melhor_trilha = None
 *
 * Para cada trilha:
 *    melhor_trilha = trilha_1
 *
 * Se trilha_i.esforço < melhor_trilha.esforço:
 *    melhor_trilha = trilha_i
 *
 * Retornar melhor_trilha
 */

const fs = require("fs");

// Read the file entrada.txt
const input = fs.readFileSync("trilha-entrada.txt", "utf8");
const lines = input.split("\n").map((texto) => texto.trim());

var contador = 0;
function getLine() {
  return lines[contador++];
}

// ler os pontos
let qtdTrilhas = getLine()
  .split(" ")
  .map((num) => parseInt(num));

// console.log(`qtdTrilhas: ${qtdTrilhas}`);
let idTrilha = 1;
let esforcoMelhorTrilha = Infinity;
let melhorTrilhaId = 0;

while (qtdTrilhas > 0) {
  // console.log(`\n ID da Trilha: ${idTrilha}`);

  let trilha = getLine()
    .split(" ")
    .map((num) => parseInt(num))
    .slice(1);
  // console.log(`62 trilha:${trilha}`);

  let pontoAtual = 0;
  let proximoPonto = 0;
  let subida = 0;
  let descida = 0;

  for (let i = 0; i < trilha.length - 1; i++) {
    pontoAtual = trilha[i];
    proximoPonto = trilha[i + 1];
    // console.log(`pontoAtual:${pontoAtual} proximoPonto:${proximoPonto}`);

    // Calcular a subida
    if (pontoAtual < proximoPonto) {
      subida += proximoPonto - pontoAtual;
      // console.log(`subida:${subida}`);
    } else {
      descida += pontoAtual - proximoPonto;
      // console.log(`descida:${descida}`);
    }
  }

  // Pegar o valor de menor esforço da trilha
  // console.log(`subida:${subida} && descida:${descida}`);
  let esforcoTrilhaAtual = Math.min(subida, descida);

  // console.log(`trilhaEsforco: ${trilhaEsforco}`);
  // se o esforco a trilha atual é menor do que a melhor trilha
  if (esforcoTrilhaAtual < esforcoMelhorTrilha) {
    esforcoMelhorTrilha = esforcoTrilhaAtual;
    melhorTrilhaId = idTrilha;
  }

  idTrilha++;
  qtdTrilhas--;
}
console.log(melhorTrilhaId);
