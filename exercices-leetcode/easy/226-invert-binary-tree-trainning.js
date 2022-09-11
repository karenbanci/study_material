/*
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]



input:     4
        l    r
        2    7
      l  r  l  r
      1  3  6  9

output:   4
        l    r
        7     2
      l  r  l  r
      9   6  3  1
*/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */

/*
Para inverter uma árvore binária, criar um ponteiro temporário que será gual o root esquerdo, o root esquerdo será igual o root direito e o root direito será o ponteiro temporário. Essa função é recursiva, então chamar ela mesmo dentro da própria função (root.left e root.right), retornar a root. Para eu fazer uma leitura em BFS (será na sequencia uma impressão na sequência de nível). Para fazer esse tipo de impressão, criarei uma fila vazia, chamarei o ponteiro atual igual a árvore, colocarei dentro dessa fila através do push. ENQUANTO tiver elementos nessa fila, o ponteiro atual será o primeiro elemento da fila. SE o atual ponteiro for da esquerda, então coloca dentro da fila o atual ponteiro da esquerda, SE o atual ponteiro for da direita, coloca dentro da fila o atual ponteiro da direita */


var invertTree = function (root) {

  let temp = root.left;
  root.left = root.right;
  root.right = temp;

  invertTree(root.left);
  invertTree(root.right);

  return root;
};

function printbfs(tree) {
  let queue = [];

  curr = tree;
  console.log("testeeeee: "+ curr)
  queue.push(curr);

  while(queue) {
    //estou pegando o ponteiro atual e dizendo que será o primeiro da fila
    curr = queue.shift();

    if(curr.left){
      queue.push(curr.left)
    }
    if(curr.right){
      queue.push(curr.right);
    }
  }

  console.log("print em BFS: " + queue);
  return queue;

}

printbfs(
  // isso é o parâmetro tree
  invertTree(
    new TreeNode(
      4,
      new TreeNode(
        2, //left
        new TreeNode(1, null, null), //left
        new TreeNode(3, null, null) //right
      ),
      new TreeNode(
        7, //rigth
        new TreeNode(6, null, null), //left
        new TreeNode(9, null, null) //right
      )
    )
  )
);
