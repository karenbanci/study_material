import express from "express";
import chalk from "chalk";
import path from "path";
import { fileURLToPath } from "url";
import livros from "./public/livro.js"; // Adjust the path if needed

const app = express();
const port = 3000;

// Define __filename and __dirname in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Parse incoming requests with URL-encoded payloads and JSON
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve static files from the "public" folder
app.use(express.static("public"));

// Define the base path for templates (adjust the relative path as needed)
const basePath = path.join(__dirname, "./templates");

// Route to handle "livros" using your livro.js module
app.use("/livros", livros);
console.log("Index.js loaded correctly, serving routes");

// Route to serve the home page (index.html)
app.get("/", (req, res) => {
  res.sendFile(`${basePath}/index.html`);
});

// Catch-all route to serve a 404 page (404.html)
app.use((req, res) => {
  res.status(404).sendFile(`${basePath}/404.html`);
});

// Error handling middleware
// app.use((err, req, res, next) => {
//   console.error(err.stack);
//   res.status(500).send("Something went wrong!");
// });
app.use((req, res, next) => {
  console.log(`Request received for ${req.url}`);
  next();
});

// Start the server
app.listen(port, () => {
  console.log(chalk.bgGreen.black(`App running on port ${port}`));
});
