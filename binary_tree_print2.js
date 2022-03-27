/*
Imprima os nós da árvore binária nível por nível, cada nível deve ser printado em uma linha separada

árvore:

              3
          5       4
           2    1   7
          9

output:
3
54
217
9

Root
left / rigth

Order:
      3 first add / first remove / first print
      5 second add / second remove / second print
      4 third add / third remove / third print
      2 fourth add / fourth remove / fourth print
      1 fifth add / fifth remove / fifth print
      7 sixth add / sixth remove / sixth print
      9 seventh add / seventh remove / seventh print

*/

let tree = {
  value: 3,
  left: {
    value: 5,
    right: {
      value: 2,
      left: {
        value: 9
      }
    },
  },
  right: {
    value: 4,
    left: {
      value: 1
    },
    right: {
      value: 7
    }
  }
};

function levelByLevel(tree) {
  let queue = [];

  // add um elemento na fila
  queue.push(tree)

  // add uma linha vazia(pulando para a linha debaixo)
  queue.push(null)

  let result = "";

  do {
    // pegando o primeiro elemento da lista
    let currentTree = queue.shift();

    // se a atual árvore for nula
    if(currentTree === null){
      result += `\n`;

      // se a lista estiver vazia
      if(queue.length === 0){
        // o algoritmo para aqui
        break;
      }
      // pula para a linha debaixo
      queue.push(null);

    } else {
      // vai imprimir o valor do atual Nó da árvore
      result+= currentTree.value;

      // se eu tiver valor a esquerda do Nó atual, adicionar na lista esse valor
      if (currentTree.left) {
        queue.push(currentTree.left);
      }
      // se eu tiver valor a direita do Nó atual, adicionar na lista esse valor
      if (currentTree.right) {
        queue.push(currentTree.right);
      }
    }
    // rodar o algoritmo enquanto for verdadeiro
  } while(true);
  console.log(result)
}

console.log("levelByLevel ---- ");
levelByLevel(tree);
