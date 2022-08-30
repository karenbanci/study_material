/*
Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:
              1
            2   3
          4  5    6
        7           8

7+8 = 15
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
*/
/**
 * @param {TreeNode} root
 * @return {number}
 */

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}
var deepestLeavesSum = function (root) {
  let queue = [];
  current = root;

  queue.push(current);
  console.log("fila: " + queue);

  let sum = 0;

  while (queue.length) {
    current = queue.shift();
    console.log("nó atual " + JSON.stringify(current));
    console.log("proximo nó -------------------------")

    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);

    // se é folha, então adicionar na soma
    if (current.left == null && current.right == null) {
      sum += current.val;
    }
  }

  return sum;
};

const root = new TreeNode(
  1,
  new TreeNode(
    2,
    new TreeNode(4, new TreeNode(7, null, null), null),
    new TreeNode(5, null, null),
    null
  ),
  new TreeNode(3, new TreeNode(6, null, new TreeNode(8, null, null), null))
);
console.log(deepestLeavesSum(root));
