/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
*/

//  Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

// let list1 = [1,2,4];
// let list2 = [1,3,4];

const list1 = {
  val: 1,
  next: {
    val: 2,
    next: {
      val: 4,
      next: null,
    },
  },
};
const list2 = {
  val: 1,
  next: {
    val: 3,
    next: {
      val: 4,
      next: null,
    },
  },
};

var mergeTwoLists = function (l1, l2) {

  let nullNode = new ListNode( );

  //lista 3
  let prev = nullNode;

  //enquanto existir lista 1 e lista 2
  while (l1 && l2) {

    // se o valor da lista 1 for maior ou igual ao valor da lista 2
    if (l1.val >= l2.val) {
      // o próximo node da lista 3 vai ser a lista 2
      prev.next = l2;

      // aqui encaminha para o próximo valor
      l2 = l2.next;

    } else {
      // o próximo node da lista 3 vai ser a lista 1
      prev.next = l1;

      // aqui encaminha para o próximo valor
      l1 = l1.next;
    }

    //está removendo o primeiro nó
    prev = prev.next;
  }


  // se uma das listas não forem nula, ele pega o nó (ou os nós) e coloca no final do prev
  prev.next = l1 || l2;
  return JSON.stringify(nullNode.next);
};

console.log(mergeTwoLists(list1, list2));

//https://docs.google.com/presentation/d/18FESY265PdjxuHjs1f6mGT_zb3Iw7uATeOdaw2R7dVQ/edit#slide=id.p
