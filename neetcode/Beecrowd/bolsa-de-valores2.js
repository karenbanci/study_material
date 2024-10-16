function maxLucro(N, C, cotacoes) {
  let menorPreco = cotacoes[0]; // O menor preço de compra até o momento
  let maxLucro = 0; // O lucro máximo encontrado

  // Percorrer as cotações a partir do segundo dia
  for (let i = 1; i < N; i++) {
    // Calcular o lucro se vendermos neste dia
    let lucro = cotacoes[i] - menorPreco - C;

    // Atualizar o lucro máximo se o atual for maior
    if (lucro > maxLucro) {
      maxLucro = lucro;
    }

    // Atualizar o menor preço de compra
    if (cotacoes[i] < menorPreco) {
      menorPreco = cotacoes[i];
    }
  }

  // Retornar o lucro máximo (ou 0 se não houver lucro)
  return maxLucro;
}

// Exemplo de uso
let N = 6;
let C = 10;
let cotacoes = [100, 120, 130, 80, 50, 40];

console.log(maxLucro(N, C, cotacoes)); // Saída: 70
