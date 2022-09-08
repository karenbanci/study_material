const SinglyLinkedListNode = class {
  constructor(nodeData) {
    this.data = nodeData;
    this.next = null;
  }
};

const SinglyLinkedList = class {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  insertNode(nodeData) {
    const node = new SinglyLinkedListNode(nodeData);

    if (this.head == null) {
      this.head = node;
    } else {
      this.tail.next = node;
    }

    this.tail = node;
  }
};

function getNumber(binary) {
  // Write your code here

  let number = 0;

  while (binary) {
    // primeiro, o operador << move para a esquerda a quantidade de bits n na representação binária (neste caso 1).
    //Depois, o operador | tem a mesma lógica do ||  || mas é utilizado para a manipulação de bits.
    number = (number << 1) | binary.data;
    binary = binary.next;
  }
  return number;
}

const list = {
  data: 0,
  next: {
    data: 0,
    next: {
      data: 1,
      next: {
        data: 1,
        next: {
          data: 0,
          next: {
            data: 1,
            next: {
              data: 0,
              next: null,
            },
          },
        },
      },
    },
  },
};
console.log(getNumber(list));
//  output= 26
