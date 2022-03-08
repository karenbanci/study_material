// Pilhas, (LIFO: Last in first out), ou seja, último a entrarné o primeiro a sair. lembrar da pilha de livros
/*
function stack() {
  let items = [];

  this.push = function(element) {
    // adicionar um novo item a pilha
    items.push(element);
  }

  this.pop = function() {
    // remover o item do topo da pilha
    return items.pop();
  }

  this.peek = function() {
    // devolve o element que está no topo da pilha
    return items[items.length - 1];
  }

  this.isEmpty = function() {
    // informa se a pilha está vazia ou não
    return items.length === 0;
  }

  this.clear = function() {
    // limpa a pilha
    items = [];
  }

  this.size = function() {
    // informar o tamanho da pilha
    return items.length
  }

  this.print = function() {
    // imprime a pilha no console
    console.log(items.toString())
  }
}
// instancia da classe stack
let pilha = new stack();

pilha.push(2);
pilha.push(4);
pilha.push(6);
pilha.push(8);
pilha.push(10);

// pilha.clear();

// console.log(pilha.isEmpty())

pilha.print()
*/

// CONVERSOR DE DECIMAL PARA BINÁRIO

function  dec2Bnin(decNumber) {
  let restStack = [],
  rest,
  binaryString = ''

  while(decNumber > 0){ // sim
    rest = Math.floor(decNumber % 2); //22 não é divisivel por 2, resto = 1
    restStack.push(rest); // primeiro resto [1,1,1,0,1]
    decNumber = Math.floor(decNumber / 2);
  }

  while(restStack.length > 0){
    binaryString += restStack.pop().toString(); //[1,0,1,1,1]
  }

  return binaryString
}

console.log(dec2Bnin(23))
