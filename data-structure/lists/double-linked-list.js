// Double linkded list

const LinkedList{
  constructor(){
    this.head = this.tail = null;
  }

  // adicionar dados no final da lista (Tail)
  append(value){
    // se a lista estiver vazia
    if(!this.tail){
      // definiremos a cabeça e a cauda para o novo nó com o valor passado para ele
      this.head = this.tail = new Node(value);
    } else {
      // vamos capturar a cauda atual em uma variável para que a cauda antiga seja igual a cauda
      let oldTail = this.tail;
      // a ponta antiga aponta para a nova
      oldTail.next = this.tail
      // a ponta da nova aponta para antiga
      this.tail.previous = oldTail;
    }
  }

  prepend(value) {
    // se a lista estiver vazia
    if(!this.head){
      this.head = this.tail = new Node(value);
    } else {
      let oldHead = this.head;
      this.head = new Node(value);
      oldHead.prev = this.head;
      this.head.next = oldHead
    }
  }
// remover a cabeça
  deletHead(value){
    if(!this.head){
      return null
    } else {
      let removedHead = this.head;
      // se apenas tiver 1 node
      if(this.head === this.tail){
        this.head = this.tail = null;
      } else {
        this.head = this.head.next;
        // queremos remover qualquer ponteiro anterior
        this.head.prev = null;
      }
      return removedHead.value
    }

  }
// remover a cauda
  deletTail(){
    if(!this.tail){
      return null
    } else {
      let removedTail = this.tail;
      // se este é o último nó da lista
      if(this.head === this.tail){
        this.head = this.tail = null;
      } else {
        this.tail = this.tail.prev;
        this.tail.next = null;
      }
      return removedTail.value
    }
  }

  search(value){
    let currentNode = this.head;

    while(currentNode){
      if(currentNode.value === value){
        currentNode
      }
      currentNode = currentNode.next;
    }
    return null
  }
}

class Node {
  constructor(value, prev, next){
    this.value = value;
    this.prev = prev || null;
    this.next = next || null;


  }
}

// vamos igualar a uma lista encadeada
let list = new LinkedList();

list.append(1);
list.append(2);
list.append(3);

list
