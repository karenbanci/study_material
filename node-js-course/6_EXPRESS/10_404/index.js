const express = require("express");
const app = express();
const port = 3000; // variável ambiente
const users = require("./users");
const path = require("path");
// ler body - toda requisicao do body é transformada em json
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(express.json());

// arquivos estáticos
app.use(express.static("public"));

const basePath = path.join(__dirname, "templates");

app.use("/users", users);

app.get("/", (req, res) => {
  //renderizar o arquivo selecionado
  res.sendFile(`${basePath}/index.html`);
});

// tudo que tiver acima dessa linha e a pasta não for encontrada, o código será executado e será exibido a pagina 404
app.use(function (req, res, next) {
  res.status(404).sendFile(`${basePath}/404.html`);
});

// recebendo a resposta, se acessar no navegador, ele vai mostrar o texto
app.listen(port, () => {
  console.log(`App rodando na porta ${port}`);
});
