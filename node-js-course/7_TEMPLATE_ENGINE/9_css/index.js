const express = require("express");
const { create } = require("express-handlebars");

const app = express();

// Create an instance of the handlebars engine
const hbs = create({
  extname: ".handlebars",
  partialsDir: ["views/partials"],
});

app.engine("handlebars", hbs.engine);
app.set("view engine", "handlebars");

app.use(express.static("public"));

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

app.get("/blog", (req, res) => {
  const posts = [
    {
      title: "Aprender Node.js",
      category: "JavaScript",
      body: "Teste",
      comments: 1,
    },
    {
      title: "Aprender React.js",
      category: "JavaScript",
      body: "Teste",
      comments: 5,
    },
    {
      title: "Aprender Python",
      category: "Python",
      body: "Teste",
      comments: 3,
    },
    {
      title: "Aprender PHP",
      category: "PHP",
      body: "Teste",
      comments: 2,
    },
  ];
  res.render("blog", { posts });
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
