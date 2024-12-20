const express = require("express");
const exphbs = require("express-handlebars");
const mysql = require("mysql2");
// const mysql = require("mysql");

const app = express();

app.use(express.urlencoded({ extended: true }));

app.use(express.json());

app.engine("handlebars", exphbs.engine({ defaultLayout: "main" }));
app.set("view engine", "handlebars");

app.use(express.static("public"));

app.get("/", (req, res) => {
  res.render("home");
});

app.post("/books/insertbook", (req, res) => {
  const title = req.body.title;
  const pageqty = req.body.pageqty;

  const sql = ` INSERT INTO books (title, pageqty) VALUES ('${title}', ${pageqty})`;

  conn.query(sql, function (err, result) {
    if (err) {
      console.log(err);
      return res.status(500).send("Erro ao inserir livro");
    }
    res.redirect("/books");
  });
});

const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Nalacarolina1",
  database: "nodemysql2",
});

conn.connect(function (err) {
  if (err) {
    console.log(err);
    return;
  }
  console.log("Conectado ao MySQL");

  app.listen(3000);
});
