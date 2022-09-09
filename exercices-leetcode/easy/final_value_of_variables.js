/*
operations = ["++X","++X","X++"]


primeiro: eu vou identificar o valor da string
"++X" e "X++" eles tem o valor de 1+
"--X" e "X--" eles tem o valor de 1-

vou pegar a string e iterar as operações para que ele vincule ao seu determinado valor

index.          0     1     2
operations = ["++X","++X","X++"]

o index 0 tem o valor de 1
o index 1 tem o valor de 1
o index 2 tem o valor de 1

 começa do index 0 e ele para até o index for o tamanho da array (operations.length)

 let x = 0

primeira iteração x vale 0
operations[0] = x incrementa +1

segunda iteração o x vale 1
operations[1] = x incrementa +1

terceira iteração o x vale 2
operations[2] = x incrementa +1

retorna o valor de x que é = 3
*/

var finalValueAfterOperations = function (operations) {
  let x = 0;
  for (let i = 0; i < operations.length; i++) {
    if ("++X" == operations[i] || "X++" == operations[i]) {
      x++;
      // console.log("A", x)
    } else {
      // caso contrario X-- ou --X
      x--;
      // console.log("B", x)
      // console.log("terceiro teste", x)
      // return x
    }
    // console.log("C", x)
  }
  return x;
};
