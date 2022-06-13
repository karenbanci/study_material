
/* Pseudocódigo

Primeiro, ter que definir o tamanho da lista

Segundo, descobrir qual é o nó do meio pelo index

Terceiro, conectar o prev com o next

*/

// AQUI É MOSTRAR PARA A FUNÇÃO QUE IREMOS FAZER UM NODE
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
};

function getByIndex(head, index) {
  let ponteiro = head; //linked list
  let count = 0; // inteiro
  // enquanto houver um ponteiro
  while (ponteiro) {
    // se a contagem for igual ao index
    if (count === index) {
      return ponteiro;
    } else {
      // caso contrário ele vai adiante até encontrar o ponteiro que eu quero
      ponteiro = ponteiro.next;
    }
    // acrescenta uma unidade a cada contagem de ponteiro
    count++;
  }
  return null;
}

var deleteMiddle = function (head) {
  let node = head;
  let size = 0;

  while (node) {
    // enquanto o o nó da lista não seja nulo, eu faço a contagem de quandos nós tem na lista
    size++;
    // to apontando para o proximo ponteiro
    node = node.next;
  }
  // colocando a condição caso a lista só tenha um único elemento, retorne nulo
  if (size === 1) {
    return null;
  }
  // aqui estou descobrindo o meio da lista
  const middleIndex = Math.round((size - 1) / 2);

  // eu vou pegar o nó que vem antes do meio da lista
  let prevNode = getByIndex(head, middleIndex - 1);

  // eu vou pegar o nó que vem depois do meio da lista
  let nextNode = getByIndex(head, middleIndex + 1);

  // conectar o prevNode com o nextNode
  prevNode.next = nextNode;

  return head;
};

// const input = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null)))))
// console.log(deleteMiddle(input))

// const input2 = new ListNode(
//   1,
//   new ListNode(
//     3,
//     new ListNode(
//       4,
//       new ListNode(7, new ListNode(1, new ListNode(2, new ListNode(6, null))))
//     )
//   )
// );
// console.log(deleteMiddle(input2));


// const input3 = new ListNode(
//   1,
//   new ListNode(
//     2,
//     new ListNode(
//       3,
//       new ListNode(4,null)
//     )
//   )
// );
// console.log(deleteMiddle(input3));


// const input4 = new ListNode(
//   2,
//   new ListNode(1, null)
// );
// console.log('retorno: ', deleteMiddle(input4));

const input5 = new ListNode(2, null);
console.log("retorno: ", deleteMiddle(input5));
