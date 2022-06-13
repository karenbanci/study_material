// Criando NODE
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.previous = null;
  }

  // set = definir (definir próximo node)
  setNextNode(node) {
    if (node instanceof Node || node === null) {
      this.next = node;
    } else {
      throw new Error("Next node must be a member of the Node class");
    }
  }

  // set = definir (definir node anterior)
  setPreviousNode(node) {
    if (node instanceof Node || node === null) {
      this.previous = node;
    } else {
      throw new Error("Previous node must be a member of the Node class");
    }
  }

  // pegar o próximo node
  getNextNode() {
    return this.next;
  }

  // pegar o node anterior
  getPreviousNode() {
    return this.previous;
  }
}

// instrucoes da LISTA BIDIRECIONAL
class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  // ADICIONAR A CABEÇA
  addToHead(data) {
    // criar uma nova cabeça da instancia de Node
    const newHead = new Node(data);
    //definindo a atual cabeça do node
    const currentHead = this.head;
    // se a cabeça tiver valor
    if (currentHead) {
      // estou pegando a atual cabeça e definindo o newHead como a cabeça anterior do atual
      currentHead.setPreviousNode(newHead);
      // estou pegando a nova cabeça e definindo a proxima cabeça seja a cabeça atual
      newHead.setNextNode(currentHead);
    }
    // estou dizendo que o cabeçado da lista agora será o newHead recém adicionada
    this.head = newHead;
    // se a lista nao tiver causa (for lista de um único nó)
    if (!this.tail) {
      // definindo que a cauda será a nova cabeça
      this.tail = newHead;
    }
  }

  // ADICIONAR A CAUDA
  addToTail(data) {
    // criando uma nova cauda a partir da instancia de NODE
    const newTail = new Node(data);
    // definindo a atual cauda
    const currentTail = this.tail;
    // se houver cauda na lista
    if (currentTail) {
      // definindo a atual cauda para a nova cauda adicionada
      currentTail.setNextNode(newTail);
      // definindo que a atual cauda seja anterior da nova cauda
      newTail.setPreviousNode(currentTail);
    }
    // estou dizendo que a cauda da lista é a noda cauda recém adicionada
    this.tail = newTail;
    // se não tiver cabeça ( a lista for um único nó)
    if (!this.head) {
      // estou definindo que a cabeça será a nova cauda
      this.head = newTail;
    }
  }

  // REMOVER CABEÇA
  removeHead() {
    // definindo a cabeça que irei remover
    const removedHead = this.head;
    // se nao tiver valor, significa não nao tem nada para remover
    if (!removedHead) {
      return;
    }
    // estou definindo que o cabeçalho da lista para o removedHead o próximo nó
    this.head = removedHead.getNextNode();
    // se a cabeça tiver valor
    if (this.head) {
      // vou definir que cabeça seguinte da cabeça que foi removida o previous node seja null
      this.head.setPreviousNode(null);
    }
    // se a cabeça removida for igual a cauda (se tiver um único nó)
    if (removedHead === this.tail) {
      // chamar o remove tail para remover o nó
      this.removeTail();
    }

    return removedHead.data;
  }

  // REMOVER A CAUDA
  removeTail() {
    // definindo a cauda que vou remover
    const removedTail = this.tail;
    // se a cauda não tiver valor, retorne
    if (!removedTail) {
      return;
    }
    // definindo o valor anterior da cauda
    this.tail = removedTail.getPreviousNode();
    //  se a cauda anterior tiver valor, vou deixar que o próximo node seja null (para que nao tenha próximo node)
    if (this.tail) {
      this.tail.setNextNode(null);
    }
    // se a cauda for igual a cabeça, quer dizer que era uma lista de um único nó
    if (removedTail === this.head) {
      //  chamar o remove head para remover o nó
      return this.removeHead();
    }
    return removedTail.data;
  }

  // REMOVER QUALQUER ELEMENTO NO MEIO DO DA LISTA
  removeByData(data) {
    // nao sabemos aonde está o node que procuramos, então não deixar nenhum valor
    let nodeToRemove;
    // a busca vai começar pela cabeça da lista
    let currentNode = this.head;

    // enquanto o atual Nó tiver algum valor (for diferente de nulo)
    while (currentNode !== null) {
      //  se o atual nó for igual ao dado que estamos procurando
      if (currentNode.data === data) {
        // então definir que o nó para remover seja o atual nó
        nodeToRemove = currentNode;
        // sair do loop
        break;
      }
      // atualizar o atual nó para verificar o próximo nó
      currentNode = currentNode.getNextNode();
    }
    // se o node para remover ter algum valor, se nao acontecer
    if (!nodeToRemove) {
      // retorne nulo
      return null;
    }

    // aqui vou verificar se o node que vou remover é a cabeça da lista
    if(nodeToRemove === this.head){
      // então vamos chamar o mótodo removeHead para remover a cabeça do nó
      this.removeHead()
      // caso contrário, verificar se o nó é a cauda da lista
    } else if (nodeToRemove === this.tail){
      // chamaremos o método removeTail para remover a cauda da lista
      this.removeTail()

      // aqui vamos mexer com os ponteiros
    } else {
      const nextNode = nodeToRemove.getNextNode();
      const previousNode = nodeToRemove.getPreviousNode();

      nextNode.setPreviousNode(previousNode);
      previousNode.setNextNode(nextNode);
    }

    return nodeToRemove;
  }

  printList() {
    let currentNode = this.head;
    let output = "<head> ";
    while (currentNode !== null) {
      output += currentNode.data + " ";
      currentNode = currentNode.getNextNode();
    }
    output += "<tail>";
    console.log(output);
  }
}

// EXEMPLO
const toDoList = new DoublyLinkedList();

toDoList.addToHead("Me arrumar para ir para a escola,");
toDoList.addToHead("Preparar o almoço,");
toDoList.addToHead("Colocar a roupa para secar,");
toDoList.addToHead("Lavar Roupa,");
toDoList.printList();

toDoList.addToTail("Fazer lição de casa ------,");
toDoList.addToTail("Estudar codecademy ------,");
toDoList.printList();

toDoList.removeHead();
toDoList.removeTail();
toDoList.removeByData("Lavar Roupa,");
toDoList.printList();
