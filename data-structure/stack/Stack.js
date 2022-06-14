const LinkedList = require("./LinkedList");

class Stack {
  constructor(maxSize = Infinity) {
    this.stack = new LinkedList();
    this.maxSize = maxSize;
    this.size = 0;
  }
// verifica o tamanho da pilha é menor que o máximo permitido
  hasRoom() {
    return this.size < this.maxSize;
  }
// verifica se a pilha está vazia
  isEmpty() {
    return this.size === 0;
  }

  // adiciona um valor ao topo da pilja
  push(value) {
    if (this.hasRoom()) {
      this.stack.addToHead(value);
      this.size++;
    } else {
      throw new Error("Stack is full");
    }
  }

  // remove o valor do topo da pilha
  pop() {
    if (!this.isEmpty()) {
      const value = this.stack.removeHead();
      this.size--;
      return value;
    } else {
      console.log("Stack is empty!");
    }
  }

  // retorna o valor do topo da pilha sem removê-lo
  peek() {
    if (!this.isEmpty()) {
      return this.stack.head.data;
    } else {
      return null;
    }
  }
}

module.exports = Stack;
