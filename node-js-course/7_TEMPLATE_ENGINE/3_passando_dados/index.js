const express = require("express");
const { create } = require("express-handlebars");

const app = express();

// Create an instance of the handlebars engine
const hbs = create({ extname: ".handlebars" });

app.engine("handlebars", hbs.engine);
app.set("view engine", "handlebars");

app.get("/", (req, res) => {
  const user = {
    name: "Karen",
    surname: "Honorio",
  };

  const palavra = "teste";
  res.render("home", { user: user, palavra });
});

app.listen(3000, () => {
  console.log("funcionando");
});
