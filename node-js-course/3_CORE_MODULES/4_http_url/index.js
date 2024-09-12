const http = require("http");

const port = 3000;

const server = http.createServer((req, res) => {
  const urlInfor = require("url").parse(req.url, true);
  const name = urlInfor.query.name;

  res.statusCode = 200;
  res.setHeader("Content-type", "text/html");
  if (!name) {
    res.end(
      '<h1>Preencha o seu nome:</h1><form method="GET"><input type="text" name="name"></input><input type="submit" value="enviar"></input></form>'
    );
  } else {
    res.end(`<h1> Seja bem vindo ${name}</h1>`);
  }
});

server.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`);
});
