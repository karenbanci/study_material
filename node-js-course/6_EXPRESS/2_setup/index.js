const express = require("express");
const app = express();
const port = 3000; // variável ambiente

// get no http - o que precisa ser feito quando o usuário acessa o site
// req = recebe , res = resposta do usuário
app.get("/", (req, res) => {
  res.send("Olá mundo!");
});

// recebendo a resposta, se acessar no navegador, ele vai mostrar o texto
app.listen(port, () => {
  console.log(`App rodando na porta ${port}`);
});
