/**
 * Toda criança certamente já brincou de “vivo ou morto”. A brincadeira é dirigida por um “chefe” (um adulto), que comanda dois ou mais participantes (crianças). A brincadeira é composta de rodadas. No início, os participantes são organizados pelo chefe em fila única. A cada rodada o chefe grita “vivo” ou “morto” e todos os participantes tentam seguir sua ordem, levantando-se ao ouvir a palavra “vivo” ou abaixando-se ao ouvir a palavra “morto”. Um participante que não segue a ordem do chefe é eliminado, deixando o seu lugar na fila. Os participantes remanescentes agrupam-se novamente em fila única, preenchendo as posições dos participantes eliminados, mas mantendo suas posições relativas. O jogo continua até que uma rodada seja composta por exatamente um participante. Tal participante é dito o vencedor do jogo.

Por exemplo, considere que a brincadeira inicie com cinco participantes, identificados por números inteiros de 1 a 5, e que o chefe organize a fila na ordem m 3 → 2 → 1 → 4 → 5. Se na primeira rodada forem eliminados os participantes 2 e 4, a fila da segunda rodada será formada por 3 → 1 → 5; se na segunda rodada for eliminado o participante 1, a fila da terceira rodada será formada por 3 → 5. Se na terceira rodada o participante 3 for eliminado, o vencedor da brincadeira será o participante 5.

Sua tarefa é escrever um programa que determine o vencedor de uma partida de “vivo ou morto”, a partir da informação das ordens dadas pelo chefe e das ações executadas pelos participantes em cada rodada.

Entrada
A entrada é constituída de vários casos de teste, cada um representando uma partida. A primeira linha de um caso de teste contém dois números inteiros P e R indicando respectivamente a quantidade inicial de participantes (2 ≤ P ≤ 100) e quantidade de rodadas da partida (1 ≤ R ≤ 100). Os participantes são identificados por números de 1 a P. A segunda linha de um caso de teste descreve a fila organizada pelo chefe, contendo P números inteiros distintos x1, x2, . . . xP , onde x1 representa o identificador do participante no primeiro lugar na fila, x2 representa o identificador do participante no segundo lugar na fila, e assim por diante (1 ≤ xi ≤ P). Cada uma das R linhas seguintes representa uma rodada, contendo um número inteiro inteiro N indicando o número de participantes da rodada (2 ≤ N ≤ P), um número inteiro inteiro J representando a ordem dada pelo chefe (0 ≤ J ≤ 1) e N números inteiros Ai representando a ação do participante colocado na i-ésima posição na fila (0 ≤ Ai ≤ 1). Ordens e ações “vivo” são representadas pelo valor 1, ordens e ações “morto” pelo valor zero. Cada partida tem exatamente um vencedor, determinado somente na última rodada fornecida no caso de teste correspondente. O final da entrada é indicado por P = R = 0.

A entrada deve ser lida do dispositivo de entrada padrão (normalmente o teclado).

Saída
Para cada caso de teste seu programa deve produzir três linhas. A primeira identifica o conjunto de teste no formato “Teste n”, onde n é numerado a partir de 1. A segunda linha deve conter o identificador do vencedor. A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.

A saída deve ser escrita no dispositivo de saída padrão (normalmente a tela).
 */

const fs = require("fs");

// Read the file entrada.txt
const input = fs.readFileSync("entrada.txt", "utf8");
const lines = input.split("\n").map((texto) => texto.trim());

// console.log("input\n", input);

var contador = 0;
function getLine() {
  return lines[contador++];
}

function eliminaJogador(fila, j) {
  fila[j] = -1;
}

function jogadorNaPartida(jogador) {
  return jogador != -1;
}

let numeroTeste = 1;

// 1) Ler os participantes e partidas
// "5 4" -> [ '5', '4' ]

let [qtdParticipantes, qtsPartidas] = getLine()
  .split(" ")
  .map((num) => parseInt(num));
// console.log("participantes", qtdParticipantes, "partidas", qtsPartidas);

while (qtdParticipantes != 0) {
  // 2) Criar a fila
  // " 3 2 1 4 5" -> ['3','2','1','4','5'] -> [3,2,1,4,5]
  let fila = getLine()
    .split(" ")
    .map((num) => parseInt(num));
  // console.log("50: fila", fila);

  // 3) Analizar as partidas
  for (let i = 0; i < qtsPartidas; i++) {
    // 3.1) Ler o comando do chefe
    let linha = getLine()
      .split(" ")
      .map((num) => parseInt(num));
    let qtdParticipanteRestante = linha[0];
    let comandoChefe = linha[1];
    let acoes = linha.slice(2);

    // 3.2) Analiza cada participante
    for (let j = 0; j < qtdParticipanteRestante; j++) {
      if (acoes[j] != comandoChefe) {
        eliminaJogador(fila, j);
      }
    }
    // 3.3) Remover os que não seguiram o comando
    fila = fila.filter(jogadorNaPartida);
    // console.log("fila 68:", fila);
  }

  console.log("Teste", numeroTeste);
  console.log(fila[0], "\n");
  numeroTeste++

  [(qtdParticipantes, qtsPartidas)] = getLine()
  .split(" ")
  .map((num) => parseInt(num));
}
