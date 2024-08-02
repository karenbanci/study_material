const fs = require("fs");

console.log("Início");

fs.writeFile("arquivo.txt", "Olá, Karen!!", (err) => {
  setTimeout(() => {
    console.log("Arquivo escrito");
  }, 1000);
});

console.log("Final do código");
