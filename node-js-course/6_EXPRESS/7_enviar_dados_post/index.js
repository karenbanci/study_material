const express = require("express");
const app = express();
const port = 3000; // variável ambiente

const path = require("path");

// ler body - toda requisicao do body é transformada em json
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(express.json());

const basePath = path.join(__dirname, "templates");

app.get("/users/add", (req, res) => {
  res.sendFile(`${basePath}/userform.html`);
});

app.post("/users/save", (req, res) => {
  console.log(req.body);

  const name = req.body.name;
  const age = req.body.age;

  console.log(`O nome do usuário ${name} e idade ${age}`);

  res.sendFile(`${basePath}/userform.html`);
});

app.get("/users/:id", (req, res) => {
  const id = req.params.id;

  // leitura da tabela de users, resgatar um usuário do banco
  console.log(`estamos buscando pelo usuário: ${id}`);
  res.sendFile(`${basePath}/users.html`);
});

// req = recebe , res = resposta do usuário
app.get("/", (req, res) => {
  //renderizar o arquivo selecionado
  res.sendFile(`${basePath}/index.html`);
});

// recebendo a resposta, se acessar no navegador, ele vai mostrar o texto
app.listen(port, () => {
  console.log(`App rodando na porta ${port}`);
});
