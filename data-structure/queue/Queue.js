const LinkedList = require("./LinkedList");

class Queue {
  // Infinity é um valor padrão para infinito
  constructor(maxSize = Infinity) {
    this.queue = new LinkedList();
    this.maxSize = maxSize;
    this.size = 0;
  }

  // determinando se a lista está vazia
  isEmpty() {
    return this.size === 0;
  }

  // determinando a lista está no limite do tamanho
  hasRoom() {
    return this.size < this.maxSize;
  }

  // adicionando um NÓ no final da fila (TAIL)
  enqueue(data) {
    // verificando se tem espaço suficiente para add um elemento da lista (evitando o Overflow)
    if (this.hasRoom()) {
      // add o nó no final da lista
      this.queue.addToTail(data);
      // aumentando a contagem de um elemento add
      this.size++;
      console.log(`Added ${data} to queue! Queue size is now ${this.size}.`);
    } else {
      throw new Error("Queue is full");
    }
  }

  // removendo o primeiro nó da fila (HEAD)
  dequeue() {
    // verificando se está vazia, não se estiver, remova
    if (!this.isEmpty()) {
      // removendo
      const data = this.queue.removeHead();
      // diminuindo a contagem do tamanho da lista
      this.size--;
      console.log(
        `Removed ${data} from queue! Queue size is now ${this.size}.`
      );
      return data;
    } else {
      throw new Error("Queue is empty!");
    }
  }
}

module.exports = Queue;

const boundedQueue = new Queue(3);

boundedQueue.enqueue(1);
boundedQueue.enqueue(2);
boundedQueue.enqueue(3);

boundedQueue.dequeue();
boundedQueue.dequeue();
boundedQueue.dequeue();
boundedQueue.dequeue();
