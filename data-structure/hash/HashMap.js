const LinkedList = require("./LinkedList");
const Node = require("./Node");

class HashMap {
  constructor(size = 0) {
    this.hashmap = new Array(size).fill(null).map(() => new LinkedList());
  }

  hash(key) {
    let hashCode = 0;
    for (let i = 0; i < key.length; i++) {
      hashCode += hashCode + key.charCodeAt(i);
    }
    // vamos comprimir o valor armazenado hashCode usando Aritmetica Modular e retornar o restante da divisão pelo comprimento de hashMap
    return hashCode % this.hashmap.length;
  }

  // assing manipulará a lógica necessária para receber um par chave-valor e armazenar o valor em um índice específico
  assign(key, value) {
    const arrayIndex = this.hash(key);
    // essa constante linkedList fará referencia à lista vinculada a qual desejamos calcular um valor
    const linkedList = this.hashmap[arrayIndex];

    if (linkedList.head === null) {
      linkedList.addToHead({ key, value });
      return;
    }

    // armazenando o nó principal da lista vinculada
    let current = linkedList.head;
    // iterar sobre a lista vinculada para encontrar a tail usando while
    while (current) {

      if (current.data.key === key) {
        current.data = { key, value };
      }

      if (!current.next) {
        current.next = new Node({ key, value });
        break;
      }
      current = current.next;
    }
  }

  // Recuperar: vamos atrivuir o valor ao índice que geramos. Deve calcular o índice da matriz da mesma maneira de assign() e em seguida recuperar o valor nesse indice
  retrieve(key) {
    const arrayIndex = this.hash(key);

    // retorna o valor armazenado em arrayIndex
    let current = this.hashmap[arrayIndex].head;

    // usaremos para iterar sobre cada nó na lista vinculada até encontrarmos o valor que estamos procurando ou chegamos no final da lista
    while (current) {
      // verifica se a chave que recebemos como argumento e a chave do nó atual são as mesmas
      if (current.data.key === key) {
        return current.data.value;
      }
      // se as chaves nao correspondem, definir o atual para o próximo nó da lista
      current = current.next;
    }
    //  se percorrermos a lista e não encontramos o valor que queremos recuperar, significa que o valor não está armazenado no mapa, retornal null
    return null;
  }
}

module.exports = HashMap;
