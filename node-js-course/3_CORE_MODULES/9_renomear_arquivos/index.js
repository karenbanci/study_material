const fs = require("fs");
const arquivoAntigo = "arquivo.txt";
const novoArquivo = "novo.txt";

fs.rename(arquivoAntigo, novoArquivo, function (err) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`O arquivo ${arquivoAntigo} foi renomeado para ${novoArquivo}`);
});
