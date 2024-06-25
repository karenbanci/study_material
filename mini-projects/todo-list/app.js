const express = require("express"); // import express
const bodyParser = require("body-parser");
const sqlite3 = require("sqlite3").verbose();
const app = express();

const db = new sqlite3.Database("./database.sqlite");

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

// create table
db.run(
  "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)"
);

// get all tasks
app.get("/", (req, res) => {
  db.all("SELECT * FROM tasks", (err, rows) => {
    if (err) {
      return console.error(err.message);
    }
    res.render("index", { tasks: rows });
  });
});

// add task
app.post("/add", (req, res) => {
  const { title } = req.body;
  db.run("INSERT INTO tasks (title) VALUES (?)", [title], (err) => {
    if (err) {
      return console.error(err.message);
    }
    res.redirect("/");
  });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
