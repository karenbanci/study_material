// const x = "10";
const x = 10;
console.log(typeof x);
// checar se x é um numero
if (!Number.isInteger(x)) {
  throw new Error("x não é um número");
}

console.log("continua o código");
