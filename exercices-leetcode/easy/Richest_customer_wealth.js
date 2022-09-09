/*
Terá uma array de arrays, tenho que determinar qual é a soma total dos valores da array que vale mais (que tem o valor mais alto)

para eu acessar a array da array


index         0.    1.    2
accounts = [[1,5],[7,3],[3,5]]
total         6.    10.   8

pegar cada index e somar os valores, retornar o maior valor

         i             i. j.            i  j
accounts[0] = accounts[0][0] + accounts[0][1]  // 6
accounts[1] = accounts[1][0] + accounts[1][1]  // 10
accounts[2] = accounts[2][0] + accounts[2][1]  // 8

depois disso, comparar qual array tem valor maior e retornar

*/

var maximumWealth = function (accounts) {
  let richestCustomer = 0;

  //     aqui estou iterando cada elemento da array
  for (let i = 0; i < accounts.length; i++) {
    //       essa variavel é para armazenar a riqueza total de cada cliente
    let customerWealth = 0;

    //      aqui estou iterando dentro da array de array
    for (let j = 0; j < accounts[i].length; j++) {
      //         aqui pego cada cliente e adiciono o total da sua riqueza em sua variavel
      customerWealth += accounts[i][j];
    }

    //      aqui eu faço comparativo de quem tem o valor maior
    richestCustomer = Math.max(richestCustomer, customerWealth);
  }
  // retorno o cliente com maior valor
  return richestCustomer;
};
