const fs = require("fs");

console.log("Início");

fs.writeFileSync("arquivo.txt", "Olá, Mundo!");

console.log("Fim");
