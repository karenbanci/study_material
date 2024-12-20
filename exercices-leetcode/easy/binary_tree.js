/*
Primeira informação é saber aonde visita o nó, se é preOrder, inOrder ou posOrder
*/

let arvore = {
  value: 10,
  left: {
    value: 5,
    left: {
      value: 9,
      right: undefined,
      left: undefined,
    },
    right: {
      value: 18,
      right: undefined,
      left: undefined,
    },
  },
  right: {
    value: 20,
    left: {
      value: 3,
      right: undefined,
      left: undefined,
    },
    right: {
      value: 7,
      right: undefined,
      left: undefined,
    },
  },
};

/* Primeira forma de navegar pela árvore
 O que a preOrder faz?
 Ela imprime o Value, depois vai para left e depois right
*/

function preOrder(tree) {
  // sempre imprime o value primeiro, value começa antes de todo mundo
  console.log(tree.value)
  // verificar se está vazio
  tree.left && preOrder(tree.left)
  tree.right && preOrder(tree.right)
}
console.log('preOrder')
preOrder(arvore)

/* ------ O que a inOrder faz?
Ele vai para a esquerda primeiro, viu que a esquerda está undefined, ai ele imprime o value 2, depois vai para a direita, imprime 3, depois ele sai do nó e vai para a direira, está undefined, ai ele imprime o valor 10
*/

function inOrder(tree) {
  // verificar se está vazio
  tree.left && inOrder(tree.left)
  // imprime o value
  console.log(tree.value)
  tree.right && inOrder(tree.right)
}
console.log('inOrder')
inOrder(arvore)

/* ------ O que a posOrder faz?
Ele vai para a esquerda primeiro, viu que a esquerda está undefined, depois vai para a direita e imprime 3, depois ele sai do nó e imprime o valor 2, sai do nó de novo e vai para a direita que está undefined, ai ele imprime o valor 10
*/

function posOrder(tree) {
  // verificar se está vazio
  tree.left && posOrder(tree.left)
  tree.right && posOrder(tree.right)
  // imprime o value
  console.log(tree.value)
}
console.log('posOrder')
posOrder(arvore);

function bfs(tree) {

  let queue = [],
    current = tree;

  queue.push(current);

  while (queue.length) {
    current = queue.shift();
    console.log(current.val);

    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }
}
