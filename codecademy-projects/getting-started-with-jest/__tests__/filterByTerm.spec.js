const filterByTerm = require("../src/filterByTerm");

// function filterByTerm(inputArr, searchTerm) {
//   // podemos construir uma expressão regular que não diferencia maiúsculas de minúsculas , ou seja, uma expressão que corresponde independentemente do caso da string
//   const regex = new RegExp(searchTerm, "i");
//   return inputArr.filter(function (arrayElement) {
//     return arrayElement.url.match(regex);
//   });
// }

// describe um método Jest para conter um ou mais testes relacionados.
// Como você pode ver, são necessários dois argumentos: uma string para descrever o conjunto de testes e uma função de retorno de chamada para encapsular o teste real.

describe("Filter function", () => {
  test("it should filter by a search term (link)", () => {
    // teste de entrada
    const input = [
      { id: 1, url: "https://www.url1.dev" },
      { id: 2, url: "https://www.url2.dev" },
      { id: 3, url: "https://www.link3.dev" },
    ];

    // teste de saída
    const output = [{ id: 3, url: "https://www.link3.dev" }];

    // matcherexpect Jest para verificar se nossa função fictícia (por enquanto) retorna o resultado esperado quando chamada. Aqui está o teste:
    expect(filterByTerm(input, "link")).toEqual(output);

    expect(filterByTerm(input, "LINK")).toEqual(output);
  });
});
