/*
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

input:     4
        2    7
      1  3  6  9

output:   4
        7     2
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
var invertTree = function (root) {

};

function printbfs(tree) {

  

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
