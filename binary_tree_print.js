// FUNÇÃO DE FILAS

function queueClass() {
  let items = [];

  this.enqueue = function (elemento) {
    // adiciona novo item
    items.push(elemento);
  };

  this.dequeue = function () {
    // remove o primeiro item da fila
    return items.shift();
  };

  this.front = function () {
    // esse metodo torna o primeiro elemento da fila
    return items[0];
  };

  this.isEmpty = function () {
    // este metodo verifica se a fila está vazia
    return items.length === 0;
  };

  this.size = function () {
    // retorna o tamanho da fila
    return items.length;
  };

  this.print = function () {
    //imprimir a fila no console
    console.log(items.toString());
  };
}

/*
Imprima os nós da árvore binária nível por nível, cada nível deve ser printado em uma linha separada

árvore:

              5
          7       6
           3    4   8
          9

output:
5
76
348
9

primeiro: isso é um objeto, farei em preOrder

Raiz
esquerda / direita

*/

let tree = {
  left: {
    right: {
      left: {
        value: 9,
      },
      value: 3,
    },
    value: 7,
  },
  right: {
    left: {
        value: 4,
    },
    right: {
        value: 8,
    },
    value: 6,
  },
  value: 5,
};

function levelByLevel(tree) {
  let queue = new queueClass();
  // adicionar o primeiro elemento da fila
  queue.enqueue(tree)
  // null vai indicar para fazer uma nova linha
  queue.enqueue(null)
  do {
    // remover o primeiro elemento da fila
    let currentTree = queue.dequeue();

    // remover primeiro elemento da fila for igual a null
    if (currentTree === null) {
      console.log('----')
      if (queue.isEmpty()) {
        break;
      }
      queue.enqueue(null);

    } else {
      console.log(currentTree.value);

      // adicionar o primeiro elemento da fila
      if (currentTree.left) {
        queue.enqueue(currentTree.left);
      }
      if (currentTree.right){
        queue.enqueue(currentTree.right);
      }
      // queue.print()
    }
  } while (true);//queue.isEmpty())
}
console.log("levelByLevel ---- ");
levelByLevel(tree);
