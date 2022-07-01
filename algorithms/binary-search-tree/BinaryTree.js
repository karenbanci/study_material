class BinaryTree {
  constructor(value, depth = 1) {
    this.value = value;
    this.depth = depth;
    this.left = null;
    this.right = null;
  }

  // adicionar e colocar um valor no local correto na árvore binária
  insert(value) {
    if (value < this.value) {
      if (!this.left) {
        this.left = new BinaryTree(value, this.depth + 1);
      } else {
        this.left.insert(value);
      }
    } else {
      if (!this.right) {
        this.right = new BinaryTree(value, this.depth + 1);
      } else {
        this.right.insert(value);
      }
    }
  }

  // recuperar um nó filho por seu valor ounull
  getNodeByValue(value) {
    if (this.value === value) {
      return this;
    } else if (this.left && value < this.value) {
      return this.left.getNodeByValue(value);
    } else if (this.right) {
      return this.right.getNodeByValue(value);
    } else {
      return null;
    }
  }

  // percorrer a árvore binária usando a opção inorder traversal
  depthFirstTraversal() {
    if (this.left) {
      this.left.depthFirstTraversal();
      console.log(this.value, this.depth);
    } else if (this.right) {
      this.right.depthFirstTraversal();
    }
  }
}

module.exports = BinaryTree;
