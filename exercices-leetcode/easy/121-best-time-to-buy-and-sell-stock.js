/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
day:             0 1 2 3 4 5
Input: prices = [7,1,5,3,6,4]
maxProfitStock = 5
comparação  1 =  7,1 = -6
comparação  2 =  1,5 = 4
comparação  3 =  1,3 = 2
comparação  4 =  1,6 = 5    -- melhor resultado
comparação  5 =  1,4 = 3

primeiro iteração - encontrar o dia com o menor valor price[i]
segunda iteração - encontrar o dia com o maior valor price[j]










O(N)

Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 */


var maxProfit = function (prices) {
  let maxProfitStock = 0;

  let indexLeft = 0;
  let indexRight = 1;

  while(indexRight < prices.length) {
    console.log(indexLeft);
    console.log(indexRight);

    if(prices[indexRight] < prices[indexLeft]) {
      indexLeft = indexRight
    } else {
      let compare = prices[indexRight] - prices[indexLeft];
      console.log('lucro:', compare);

      if(compare > maxProfitStock){
        maxProfitStock = compare;
      }
    }
    indexRight++
  }
  return maxProfitStock
}

//  ----- aqui o algoritmo leva maior tempode execução
// var maxProfit = function (prices) {
//   let maxProfitStock = 0;

//   for(let i = 0; i < prices.length; i++){
//     for(let j = prices.length - 1; j > i; j--){
//       const buy = prices[i];
//       // console.log('comprou dia:', i)
//       // console.log("comprou por:", buy);

//       const sell = prices[j];
//       // console.log("vendeu dia:", j);
//       // console.log("vendeu por:", sell);


//       const compareStock = sell - buy;
//       // console.log("o lucro máximo foi:", maxProfitStock);

//       if (maxProfitStock < compareStock) {
//         maxProfitStock = compareStock;
//       }
//     }
//   }
//   return maxProfitStock
// }

const prices = [7, 1, 5, 3, 6, 4];
console.log(maxProfit(prices));
