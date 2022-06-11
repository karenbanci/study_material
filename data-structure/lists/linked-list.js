/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
/*
----------------- primeiro passo
Descobrir se a lista tem um proximo elemento
Se tiver, contar como +1
Proximo passo é descobrir se tem um proximo elemento após o head
Se tiver, contar +1
Seguir até a contagem total de elementos

----------------- segundo passo
Pegar o valor total de numeros de elementos e dividir por 2 para descobrir o medio da lista
Usar o Math.round() para arredondar para cima

----------------- terceiro passo
Apos descobrir o meio da lista, imprimir do meio em diante

*/

function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

function getByIndex(head, index){
  let ponteiro = head; // linked list
  let count = 0; //inteiro
  // enquanto houver um ponteiro
  while(ponteiro){
    // se a contagem for igual ao index
    console.log(count)
    if(count === index){
      // retorna o ponteiro
      return ponteiro;
    } else {
      // caso contrário ele vai adiante até encontrar o ponteiro que eu quero
      ponteiro = ponteiro.next;
    }
    // acrescenta uma unidade a cada contagem de ponteiro
    count++;
  }
}
const input1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5,null))))); //[1, 2, 3, 4, 5];
console.log('getByIndex', getByIndex(input1, 3));


var middleNode = function (head) {
// node é o ponteiro
  let node =  head;
  let size = 0;
  console.log(node);

    while(node){
      size++;
      // to apontando para o proximo ponteiro
      node = node.next;
      console.log("size: ", size);

    }

    const middleIndex = Math.round((size -1) / 2) ; //integer
    console.log(middleIndex);


  const middleToEnd = getByIndex(head, middleIndex);

  return middleToEnd;
};

const input = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5,null))))); //[1, 2, 3, 4, 5];
// output = new ListNode(3, new ListNode(4, new ListNode(5,null))
console.log(middleNode(input));
