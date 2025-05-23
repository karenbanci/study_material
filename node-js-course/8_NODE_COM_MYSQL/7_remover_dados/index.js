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

// criar um livro
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

// ler todos os livros
app.get("/books", (req, res) => {
  const sql = "SELECT * FROM books";

  conn.query(sql, function (err, result) {
    if (err) {
      console.log(err);
      return res.status(500).send("Erro ao buscar livros");
    }
    const books = result;

    console.log(books);

    res.render("books", { books });
  });
});

// pegar um livro específico
app.get("/books/:id", (req, res) => {
  const id = req.params.id;

  const sql = `SELECT * FROM books WHERE id = ${id}`;

  conn.query(sql, function (err, result) {
    if (err) {
      console.log(err);
      return res.status(500).send("Erro ao buscar livro");
    }

    const book = result[0];

    res.render("book", { book });
  });
});

// aditar dados
app.get("/books/edit/:id", (req, res) => {
  const id = req.params.id;

  const sql = `SELECT * FROM books WHERE id = ${id}`;

  conn.query(sql, function (err, result) {
    if (err) {
      console.log(err);
      return res.status(500).send("Erro ao buscar livro");
    }

    const book = result[0];

    res.render("editbook", { book });
  });
});

// atualizar dados no banco de dados
app.post("/books/updatebook", (req, res) => {
  const id = req.body.id;
  const title = req.body.title;
  const pageqty = req.body.pageqty;

  const sql = `UPDATE books SET title = '${title}', pageqty = '${pageqty}' WHERE id = '${id}'`;

  conn.query(sql, function (err, result) {
    if (err) {
      console.log(err);
      return res.status(500).send("Erro ao atualizar livro");
    }
    res.redirect("/books");
  });
});

// remover dados
app.get("/books/remove/:id", (req, res) => {
  const id = req.params.id;

  const sql = `DELETE FROM books WHERE id = '${id}'`;

  conn.query(sql, function (err) {
    if (err) {
      console.log(err);
      return res.status(500).send("Erro ao remover livro");
    }

    console.log("Livro removido com sucesso");
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
