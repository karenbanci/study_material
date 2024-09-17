const express = require("express");
const path = require("path");

const router = express.Router();

const basePath = path.join(__dirname, "../templates");

router.get("/add", (req, res) => {
  res.sendFile(`${basePath}/userform.html`);
});

router.post("/save", (req, res) => {
  console.log(req.body);

  const name = req.body.name;
  const age = req.body.age;

  console.log(`O nome do usuário ${name} e idade ${age}`);

  res.sendFile(`${basePath}/userform.html`);
});

router.get("/:id", (req, res) => {
  const id = req.params.id;

  // leitura da tabela de users, resgatar um usuário do banco
  console.log(`estamos buscando pelo usuário: ${id}`);
  res.sendFile(`${basePath}.html`);
});

module.exports = router;
