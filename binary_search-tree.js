/*
A diferença entre árvore binária e árvore de busca binária é que:

ÁRVORE BINÁRIA: insere os nós dentro da árvore sem nenhuma regra de inserção.

ÁRVOE BINÁRIA DE BUSCA: tem a raiz, insere o valor na raiz, quando insere o segundo valor se for maior que o valor da raiz, então insere a direita, se for menor insere a esquerda.

raiz:           1
              0   2
                    3
*/

const arvore = {}

function insert(tree, value) {
  // se a arvore tem algum valor
  if (tree.value) {
    // checar se o valor for maior que o valor da raiz
    if (value > tree.value) {
      //  se for maior que a raiz,ele insere o valor a direita
      insert(tree.right, value)
    } else {
      // se for menor que a raiz, insere o valor a esquerda
      insert(tree.left, value)
    }
  } else {
      tree.value = value
      // arvores vazias
      tree.right = {}
      tree.left = {}
  }
}
insert(arvore, 10)
insert(arvore, 11)
insert(arvore, 9)
insert(arvore, 8)

// console.log(arvore)


/* A COMPLEXIDADE DESSE ALGORITMO É  => O(log(n))

é muito fácil chegar nessa solução, pq se eu tiver 16 elementos, farei somente 4 buscas para achar o resultado, por isso log(n)
*/

function search(tree, value) {
  // se o valor da arvore não tiver nada (undefined) ou se o valor for igual o valor da busca
  if (!tree.value || tree.value === value) {
    return tree.value
  }
  if (value < tree.value) {
    return search(tree.left, value)
  }
  // aqui certamente ele é maior que o valor
  return search(tree.right, value)
}
console.log(search(arvore, 14))
console.log(search(arvore, 10));
