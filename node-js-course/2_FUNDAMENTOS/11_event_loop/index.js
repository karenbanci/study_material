// node lê o codigo de cima para baixo, mas não executa tudo de uma vez, ele executa linha por linha

function a() {
  console.log("Executando a()");
}

function b() {
  console.log("Executando b()");
}

function c() {
  console.log("Executando c()");
  a();
  b();
}

c();
