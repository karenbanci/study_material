class MinHeap {
  constructor() {
    this.heap = [null];
    this.size = 0;
  }

  add(value) {
    this.heap.push(value);
    this.size++;
    this.bubbleUp();
  }

  popMin() {
    // verificar se o heap está vazio, se tiver, retorne null
    if (this.size === 0) {
      return null;
    }

    // pegando o elemento de valor mínimo no index 1
    const min = this.heap[1];

    // apontando que o elemento de index 1 será o último (fazendo uma troca de posição)
    this.heap[1] = this.heap[this.size];
    // diminuir o tamanho da HEAP
    this.size--;
    // removendo o último elemento
    this.heap.pop();
    // invocando a heapify
    this.heapify();
    return min;
  }

  bubbleUp() {
    // aqui apontará para o indice do elemento adicionado, que é o final de heap
    let current = this.size;
    // existe um índice atual válido que seja maior que 1 && o índice atual é menor que o índice de seu pai
    while (current > 1 && this.heap[getParent(current)] > this.heap[current]) {
      // SWAP é um método auxiliar que vai trocar o índice pai pelo atual
      this.swap(current, getParent(current));
      // agora o índice atual é o PAI
      current = getParent(current);
    }
  }
//  o heap vai passar de filho esquerdo e direito para fazer as trocas
  heapify() {
    let current = 1;
    let leftChild = getLeft(current);
    let rightChild = getRight(current);
    // Check that there is something to swap (only need to check the left if both exist)
    while (this.canSwap(current, leftChild, rightChild)) {
      // Only compare left & right if they both exist
      if (this.exists(leftChild) && this.exists(rightChild)) {
        // Make sure to swap with the smaller of the two children
        if (this.heap[leftChild] < this.heap[rightChild]) {
          this.swap(current, leftChild);
          current = leftChild;
        } else {
          this.swap(current, rightChild);
          current = rightChild;
        }
      } else {
        // If only one child exist, always swap with the left
        this.swap(current, leftChild);
        current = leftChild;
      }
      leftChild = getLeft(current);
      rightChild = getRight(current);
    }
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  exists(index) {
    return index <= this.size;
  }

  canSwap(current, leftChild, rightChild) {
    // Check that one of the possible swap conditions exists
    return (
      (this.exists(leftChild) && this.heap[current] > this.heap[leftChild]) ||
      (this.exists(rightChild) && this.heap[current] > this.heap[rightChild])
    );
  }
}

const getParent = (current) => Math.floor(current / 2);
const getLeft = (current) => current * 2;
const getRight = (current) => current * 2 + 1;

module.exports = MinHeap;
