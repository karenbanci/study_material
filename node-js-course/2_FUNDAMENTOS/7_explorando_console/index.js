// npm init
// npm install minimist
// comando: node .\index.js --a=5 --b=10

const x = 10;
const y = "Karen";
const z = [1, 2, 3];

console.log(x, y, z);

// contagem de impressões, muito bom para debugar loops
console.count(x);
console.count(x);
console.count(x);
console.count(x);

// variavel entre string , converte para string
console.log("o nome é %s, ela é programadora", y);
console.log(`o nome é ${y}, ela é programadora`);

// limpar console
setTimeout(() => {
  console.clear();
}, 2000);
