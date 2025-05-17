const express = require("express");
const exphbs = require("express-handlebars");
const conn = require("./db/conn");

const User = require("./models/User");

const app = express();

app.use(express.urlencoded({ extended: true }));

app.use(express.json());

app.engine("handlebars", exphbs.engine({ defaultLayout: "main" }));
app.set("view engine", "handlebars");

app.use(express.static("public"));

app.get("/users/create", (req, res) => {
  res.render("adduser");
});

// criar um usuário
// o método post é usado para enviar dados para o servidor
app.post("/users/create", async (req, res) => {
  const name = req.body.name;
  const occupation = req.body.occupation;
  let newsletter = req.body.newsletter;

  if (newsletter === "on") {
    newsletter = true;
  } else {
    newsletter = false;
  }

  await User.create({ name, occupation, newsletter });

  res.redirect("/");
});

// mostrar o conteúdo do usuário
app.get("/users/:id", async (req, res) => {
  const id = req.params.id;

  // where = filtrar os dados, findOne = encontrar um único dado
  const user = await User.findOne({ where: { id: id }, raw: true });

  res.render("userview", { user: user });
});

// delete
app.post("/users/delete/:id", async (req, res) => {
  const id = req.params.id;

  await User.destroy({ where: { id: id } });

  res.redirect("/");
});

// editar
app.get("/users/edit/:id", async (req, res) => {
  const id = req.params.id;

  const user = await User.findOne({ raw: true, where: { id: id } });
  console.log("estamos editando o usuário: " + user.name);
  res.render("useredit", { user });
});

// atualizar o usuário
app.post("/users/update", async (req, res) => {
  const id = req.body.id;
  const name = req.body.name;
  const occupation = req.body.occupation;
  let newsletter = req.body.newsletter;

  if (newsletter === "on") {
    newsletter = true;
  } else {
    newsletter = false;
  }

  const userData = {
    id,
    name,
    occupation,
    newsletter,
  };
  console.log("editado o usuário: " + userData.name);

  await User.update(userData, { where: { id: id } });
  res.redirect("/");
});

// ler todos os usuários
app.get("/", async (req, res) => {
  const users = await User.findAll({ raw: true });

  // console.log(users);

  res.render("home", { users: users });
});

// criar o banco de dados
// o método sync() é usado para sincronizar o banco de dados com o modelo
conn
  // .sync({ force: true }) // recria do banco de dados e vai apagar os dados existentes
  .sync()
  .then(() => {
    app.listen(3000, () => {
      console.log("Servidor rodando na porta 3000");
    });
  })
  .catch((err) => {
    console.log("Erro ao conectar ao banco de dados: " + err);
  });
