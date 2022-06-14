//CLASSE FILA

function queue() {
  let items = [];

  this.enqueue = function(elemento){
    // adiciona novo item
    items.push(elemento);
  }

  this.dequeue = function() {
    // remove o primeiro item da fila
    return items.shift();
  }

  this.front = function () {
    // esse metodo torna o primeiro elemento da fila
    return items[0];
  }

  this.isEmpty = function () {
    // este metodo verifica se a fila está vazia
    return items.length === 0
  }

  this.size = function () {
    // retorna o tamanho da fila
    return items.length
  }

  this.print = function () {
    //imprimir a fila no console
    console.log(items.toString())
  }
}
