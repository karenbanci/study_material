import express from "express";
import chalk from "chalk";
import path from "path";
import { fileURLToPath } from "url"; // Import for handling __dirname in ES modules

const router = express.Router();

// Define __filename and __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Define the base path for templates
const basePath = path.join(__dirname, "../templates");
console.log("Livro.js router is being used");

router.get("/", (req, res) => {
  res.sendFile(`${basePath}/livroform.html`);
});

// Route to serve the form for adding a book
router.get("/add", (req, res) => {
  console.log("The /livros/add route was accessed");
  // res.sendFile(`${basePath}/livroform.html`);
  res.redirect("/livros");
});

// Route to handle form submission
router.post("/save", (req, res) => {
  console.log(chalk.bgYellow.black(req.body)); // Logs the form data to console

  // Send the form page back as response
  res.sendFile(`${basePath}/livroform.html`);
});

// Route to handle dynamic user requests by ID
router.get("/:id", (req, res) => {
  const id = req.params.id;

  // Simulate looking up the user in the database
  console.log(`Estamos buscando pelo usuário: ${id}`);

  // Fix the path here to send a valid HTML file for the user page
  res.sendFile(`${basePath}/livroform.html`);
});

export default router;
