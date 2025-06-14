const express = require("express");
const exphbs = require("express-handlebars");
const app = express();
const conn = require("./db/conn");

app.engine("handlebars", exphbs.engine({ defaultLayout: "main" }));
app.set("view engine", "handlebars");

app.use(
  express,
  express.urlencoded({
    extended: true,
  })
);

app.use(express.json());

app.use(express.static("public"));

app.listen(3000);
