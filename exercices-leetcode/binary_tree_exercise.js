/*
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */


let root1 = [1,3,2,5]
let root2 = [2,1,3,null,4,null,7]


function preOrder(tree) {
  // sempre imprime o value primeiro, value começa antes de todo mundo
  console.log(tree.val)
  // verificar se está vazio
  tree.left && preOrder(tree.left)
  tree.right && preOrder(tree.right)
}

var mergeTrees = function(root1, root2) {

// se existir raiz1 e raiz2
    if (root1 && root2) {

// aqui vou somar os valores das raízes
        let sum = root1.val + root2.val

//  criando uma nova arvore, TreeNode(val, left, right)  é a arvore, entao sum é soma das raízes, mergeTree(pegando a arvore atual e combinando os valores de cada arvore (sub-árvore) )
        let result = new TreeNode(sum, mergeTrees(root1.left, root2.left), mergeTrees(root1.right, root2.right))

        return result

    } else if (root1 ){
//         se o root1 existe, vai retornar root1
        return root1
    } else if (root2){
//         se o root2 existe, vai retornar root2
        return root2
    } else {
        return null
    }
};
