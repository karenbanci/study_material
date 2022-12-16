/*
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have  reference to its parent node. The definition for node is below:

class Node {
  public int val;
  public Node left;
  public Node right;
  public Node parent;
}

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)"

Example 1:
              3
            5   1
          6  2  0  8
            7 4

input: root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5 and q = 1
output: 3

Explanation: The LCA of nodes 5 and 1 is 3;

Example 2:
            3
          5   1
        6  2 0 8
          7 4

input: root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5 and q = 4
output: 5

Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
*/

// class Node {
//   public int val;
//   public Node left;
//   public Node right;
//   public Node parent;
// }

function TreeNode(val, left, right, parent) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
  this.parent = parent === undefined ? null : parent;
}
TreeNode.prototype.toString = function () {
  return "val=" + this.val;
};

// Tarefa de casa: Implementar com Set()
function lowestCommonAncestor(p, q) {
  const pInicial = p;
  const qInicial = q; // INITIAL

  // O(Hˆ2) time, O(1) space
  // H = logN for balanced trees
  // O(x) = C1 * x + C2
  while (p != null) {
    while (q != null) {
      if (p == q) {
        return q;
      } else {
        q = q.parent;
        console.log("q = " + q);
      }
    }
    q = qInicial;
    p = p.parent;
    console.log("p = " + p);
  }

  // antigo:

  // if (p == q) {
  //   return p;
  // } else {
  //   p = p.parent;

  //   if (p != q) {
  //     q = q.parent;

  //     if (p == q) {
  //       return p;
  //     } else {
  //       p = pInicial;

  //       if (p == q) {
  //         return p;
  //       } else {
  //         q = q.parent;

  //         if (p == q) {
  //           return p;
  //         }
  //       }
  //     }
  //   }
  // }
}

let p, q;

let treeRoot = new TreeNode(3, null, null, null);

// Children of Node Root (3)

let node5 = new TreeNode(5, null, null, treeRoot);
treeRoot.left = node5;

let node1 = new TreeNode(1, null, null, treeRoot);
treeRoot.right = node1;

// Children of Node 5

let node6 = new TreeNode(6, null, null, node5);
node5.right = node6;

let node2 = new TreeNode(2, null, null, node5);
node5.left = node2;

// Children of Node 1

let node0 = new TreeNode(0, null, null, node1);
node1.left = node0;

let node8 = new TreeNode(8, null, null, node1);
node1.right = node8;

// Children of Node 2

let node7 = new TreeNode(7, null, null, node2);
node2.left = node7;

let node4 = new TreeNode(4, null, null, node2);
node2.right = node4;

console.log("----------------------------- ex 1:");

p = node5;
q = node1;
console.log("retorna: " + lowestCommonAncestor(p, q));
console.log("esperado: 3");

console.log("----------------------------- ex 2:");

p = node5;
q = node4;
console.log("retorna: " + lowestCommonAncestor(p, q));
console.log("esperado: 5");

console.log("----------------------------- ex 3:");

p = new TreeNode(
  3,
  new TreeNode(1, null, null, null),
  new TreeNode(2, null, null, null),
  null
);
q = p;
console.log("retorna: " + lowestCommonAncestor(p, q));
console.log("esperado: 3");

console.log("----------------------------- ex 4:");

p = node7;
q = node8;
console.log("retorna: " + lowestCommonAncestor(p, q));
console.log("esperado: 3");

console.log("----------------------------- ex 5:");

p = node6;
q = node4;
console.log("retorna: " + lowestCommonAncestor(p, q));
console.log("esperado: 5");

console.log("-----------------------------");

console.log("----------------------------- ex 6:");

p = node5;
q = node2;
console.log("retorna: " + lowestCommonAncestor(p, q));
console.log("esperado: 5");

console.log("-----------------------------");
