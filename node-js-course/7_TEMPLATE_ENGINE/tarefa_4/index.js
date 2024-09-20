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

const posts = [
  {
    title: "Título do Primeiro Post",
    date: "19 de setembro de 2024",
    image: "../images/1.webp",
    id: "one",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor vehicula ",
  },
  {
    title: "Título do Segundo Post",
    date: "18 de setembro de 2024",
    image: "../images/2.webp",
    id: "two",
    content:
      "uisque ac leo ut nisi scelerisque posuere. Nam id nunc quis mi mollis venenatis ",
  },
  {
    title: "Título do Terceiro Post",
    date: "17 de setembro de 2024",
    image: "../images/3.webp",
    id: "tree",
    content:
      "Maecenas in justo in leo efficitur aliquam. Etiam suscipit magna vel tortor tincidunt ",
  },
];

app.get("/post/:slug", function (req, res) {
  const postId = req.params.slug;
  const post = posts.find((p) => p.id === postId);
  if (post) {
    res.render("post", { post });
  } else {
    res.status(404).send("Post not found");
  }
});

app.get("/sobre", (req, res) => {
  const sobre =
    "A Chemist with a Bachelor's degree and a decade of experience in Chemistry. I decided to change my career to move into the technology area in 2021 after the Web Development Bootcamp at Le Wagon in São Paulo, Brazil. In this course, I learned Ruby as my first programming language.In 2022, I moved to Silicon Valley in the United States to start my new journey as a software developer. Since then, I have improved my software development skills by studying Computer Science at Foothill College. I developed an AI application from scratch using neural networking in Python (It utilizes technology resembling the human brain, allowing autonomous predictions or decisions). I also have improved my frontend skills using ThreeJS. I enjoyed developing 3D objects on Blender and implementing them on websites with JavaScript, React, ThreeJs, and Vite. I have some projects with websites in 3D. Eager for fresh challenges, I'm open to new opportunities in software development.";

  res.render("sobre", { sobre });
});

app.get("/", (req, res) => {
  const content = {
    title: "HOME PAGE",
    subtitle: "Página de Viagens",
  };

  res.render("home", { content, posts });
});

app.listen(3000, () => {
  console.log("funcionando");
});
