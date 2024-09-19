const express = require("express");
const { create } = require("express-handlebars");

const app = express();

// Create an instance of the handlebars engine
const hbs = create({ extname: ".handlebars" });

app.engine("handlebars", hbs.engine);
app.set("view engine", "handlebars");

app.get("/", (req, res) => {
  res.render("home");
});

app.listen(3000, () => {
  console.log("funcionando");
});
