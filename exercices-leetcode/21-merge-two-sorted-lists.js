/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
*/

//  Definition for singly-linked list.
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

// let list1 = [1,2,4];
// let list2 = [1,3,4];

 const list1 = {
  val: 1,
  next: {
    val: 2,
    next: {
      val: 4,
      next: null
    }
  }
}
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


var mergeTwoLists = function(list1, list2) {
  let newList = new ListNode();
  console.log("lista 3 ", newList);
  const dummy = newList

  while(list1 && list2){
    // compare if value to list1 is less than value to list2
    if(list1.val < list2.val){
      newList.next = list1;
      list1 = list1.next;
    } else {
      newList.next = list2;
      list2 = list2.next;
    }
    newList = newList.next
  }
  if(list1){
    newList.next = list1;
  }
  if(list2){
    newList.next = list2;
  }
  console.log(JSON.stringify(dummy))
  return dummy.next
};

console.log(mergeTwoLists(list1, list2))
