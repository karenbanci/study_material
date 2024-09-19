const express = require("express");
const { create } = require("express-handlebars");

const app = express();

// Create an instance of the handlebars engine
const hbs = create({ extname: ".handlebars" });

app.engine("handlebars", hbs.engine);
app.set("view engine", "handlebars");

app.get("/dashboard", (req, res) => {
  const items = ["item a", "item b", "item c"];

  res.render("dashboard", { items });
});

app.get("/post", (req, res) => {
  const post = {
    title: "Aprender Node.js",
    category: "JavaScript",
    body: "Este artigo vai te ajudar",
    comments: 4,
  };
  res.render("blogpost", { post });
});

app.get("/", (req, res) => {
  const user = {
    name: "Karen",
    surname: "Honorio",
  };

  const palavra = "teste";

  const auth = true;
  const approved = true;

  res.render("home", { user: user, palavra, auth, approved });
});

app.listen(3000, () => {
  console.log("funcionando");
});
