class TreeNode {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  addChild(child) {
    if (child instanceof TreeNode) {
      this.children.push(child);
    } else {
      this.children.push(new TreeNode(child));
    }
  }

  removeChild(childToRemove) {
    const length = this.children.length;
    // Se o filho alvo não for encontrado no children array, então teríamos que descer outro nível percorrendo cada filho no array e repetir o processo.
    this.children = this.children.filter((child) => {
      return childToRemove instanceof TreeNode
        ? child !== childToRemove
        : child.data !== childToRemove;
    });

    if (length === this.children.length) {
      this.children.forEach((child) => child.removeChild(childToRemove));
    }
  }

  print(level = 0) {
    let result = "";
    for (let i = 0; i < level; i++) {
      result += "-- ";
    }
    console.log(`${result}${this.data}`);
    this.children.forEach((child) => child.print(level + 1));
  }

  // For each node
  // Display its data
  // For each child in children, call itself recursively
  depthFirstTraversal() {
    console.log(this.data);
    this.children.forEach((child) => child.depthFirstTraversal());
  }

  // Assign an array to contain the current root node
  // While the array is not empty
  // Extract the first tree node from the array
  // Display tree node's data
  // Append tree node's children to the array

  breadthFirstTraversal() {
    let queue = [this];
    while (queue.length > 0) {
      // extraia o primeiro elemento dentro queue
      const current = queue.shift();
      // atribua-o a uma constvariável, current. Fazemos isso para que possamos exibi-lo datadepois.
      console.log(current.data);
      // mescle os currentfilhos do nó da árvore queuee reatribua a fusão a queue. Fazemos isso para que possamos percorrer os filhos do nó atual após terminarmos de percorrer seus irmãos.
      queue = queue.concat(current.children);
    }
  }
}

module.exports = TreeNode;
