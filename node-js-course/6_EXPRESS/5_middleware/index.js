const express = require("express");
const app = express();
const port = 3000; // variável ambiente

const path = require("path");

const basePath = path.join(__dirname, "templates");

const checkAuth = function (req, res, next) {
  req.authStatus = true;

  if (req.authStatus) {
    console.log("está logado!");
    next();
  } else {
    console.log("nao está logado, faça um login para continuar");
    next();
  }
};

app.use(checkAuth);

// get no http - o que precisa ser feito quando o usuário acessa o site
// req = recebe , res = resposta do usuário
app.get("/", (req, res) => {
  //renderizar o arquivo selecionado
  res.sendFile(`${basePath}/index.html`);
});

// recebendo a resposta, se acessar no navegador, ele vai mostrar o texto
app.listen(port, () => {
  console.log(`App rodando na porta ${port}`);
});
