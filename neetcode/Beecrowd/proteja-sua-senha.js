const fs = require("fs");

// Read the file entrada.txt
const input = fs.readFileSync("proteja-sua-senha.txt", "utf8");
const lines = input.split("\n").map((texto) => texto.trim());

var contador = 0;
function getLine() {
  return lines[contador++];
}

// quantidade de teste
let numeroDeAssociacoes = getLine()
  .split(" ")
  .map((num) => parseInt(num));

let numeroTeste = 1;

console.log("Teste", numeroTeste);

let valores = getLine()
  .split(" ")
  .map((val) => val);

let associacoes = [];

// pegar a senha e retorna o valor correspondente para cada tentativa
for (let tentativa = 0; tentativa < numeroDeAssociacoes; tentativa++) {
  // console.log("linha", valores);

  // SEPARAR OS NUMEROS E AS SENHAS
  let numeros = valores.slice(0, 10);
  let senha = valores.slice(10);

  let valoresSenha = valoresDaSenha(numeros, senha);

  valores = getLine()
    .split(" ")
    .map((val) => val);

  associacoes.push({ senha, valoresSenha });

  console.log(`Senha: ${senha} \nValores da senha:`, valoresSenha);
  // console.log(valorDigito);
  // console.log("\n\n---------------------------------------");
}

let tamanhoDaSenha = 6;

console.log("linha 51", associacoes);

// percorrer cada posicao da senha processar definir o valor
let stringLinha = "";

for (let posicao = 0; posicao < tamanhoDaSenha; posicao++) {
  let possibilidadesDoDigito = associacoes.map(
    (tentativa) => tentativa.valoresSenha[posicao]
  );

  stringLinha += digitoCorreto(possibilidadesDoDigito) + " ";
  // console.log("possibilidadesDoDigito", possibilidadesDoDigito);
}

console.log(stringLinha);

function digitoCorreto(possibilidadesDoDigito) {
  //[...] converte em array para usar o metodo reduce
  return [...possibilidadesDoDigito].reduce((acc, curr) =>
    [...acc].filter((x) => curr.has(x))
  )[0];
}

function senhaPadrao(numeros) {
  let padrao = {
    A: new Set(),
    B: new Set(),
    C: new Set(),
    D: new Set(),
    E: new Set(),
  };

  let chaves = Object.keys(padrao); // Obter as chaves do objeto padrao
  let chaveIndex = 0; // Índice para iterar ciclicamente sobre as chaves

  for (let i = 0; i < numeros.length; i += 2) {
    let par = numeros.slice(i, i + 2); // Obter o par de números

    // Adicionar os números individuais ao Set da chave atual
    let chave = chaves[chaveIndex];
    par.forEach((num) => padrao[chave].add(Number(num))); // Adiciona cada número separadamente

    // Atualizar o índice da chave para o próximo (cíclico)
    chaveIndex = (chaveIndex + 1) % chaves.length;
  }

  // console.log("senha padrao", padrao);
  return padrao;
}

// retorna os valores das senha correspondente
function valoresDaSenha(numeros, senha) {
  let padrao = senhaPadrao(numeros); // Função que cria o objeto padrao
  let letra = senha; // Senha que contém as letras (chaves a serem buscadas)

  let key = Object.keys(padrao); // Obtem as chaves do objeto padrao
  let val = Object.values(padrao); // Obtem os valores do objeto padrao

  let valor = [];

  for (let i = 0; i < letra.length; i++) {
    for (let j = 0; j < key.length; j++) {
      if (letra[i] === key[j]) {
        // Se a letra da senha corresponde à chave, pegar o valor correspondente
        let setValores = new Set(Array.from(val[j]));
        valor.push(setValores);
      }
    }
  }

  return valor;
}

numeroTeste++;
