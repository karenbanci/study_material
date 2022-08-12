/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

( ) list1 = [1,2,4], list2 = [1,3,4], ret = []

list1 or list2 have elements? yes
list2 have elements? yes
is the 1st element of list1 < 1st element of list2? => 1 < 1? no (list2)
then: grab the 1st element of list2 and put on ret
(1) list1 = [1,2,4], list2 = [3,4], ret = [1]

list1 or list2 have elements? yes
list2 have elements? yes
is the 1st element of list1 < 1st element of list2? => 1 < 3? yes
then: grab the 1st element of list1 and put on ret
(2) list1 = [2,4], list2 = [3,4], ret = [1,1]

list1 or list2 have elements? yes
list2 have elements? yes
is the 1st element of list1 < 1st element of list2? => 2 < 3? yes
then: grab the 1st element of list1 and put on ret
(3) list1 = [4], list2 = [3,4], ret = [1,1,2]

list1 or list2 have elements? yes
list2 have elements? yes
is the 1st element of list1 < 1st element of list2? => 4 < 3? no (list2)
then: grab the 1st element of list2 and put on ret
(4) list1 = [4], list2 = [4], ret = [1,1,2,3]

list1 or list2 have elements? yes
list2 have elements? yes
is the 1st element of list1 < 1st element of list2? => 4 < 4? no (list2)
then: grab the 1st element of list2 and put on ret
(5) list1 = [4], list2 = [], ret = [1,1,2,3,4]

list1 or list2 have elements? yes
list2 have elements? no
then: grab the list1 and put on ret
(6) list1 = [], list2 = [], ret = [1,1,2,3,4,4]

list1 or list2 have elements? no
return ret

Generalizing
============
while list1 or list2 have elements? yes
  list2 have elements? yes
    is the 1st element of list1 < 1st element of list2?
      yes then: grab the 1st element of list1 and put on ret
      no (list2) then: grab the 1st element of list2 and put on ret
    list 2 have no elements:
      then: grab the 1st element of list1 and put on ret
    list 1 have no elements:
      then: grab the 1st element of list2 and put on ret

return ret

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

var getLastElementOfList = function (list) {
   var lastOfRet = list; // 7  8  9
   var retNext = lastOfRet.next; // 8  9  null
   while (retNext) {
     // t  t  f
     lastOfRet = retNext; // 8  9
     retNext = retNext.next; // 9  null
   }
   return lastOfRet;
}

var grab1stElemOfXAndPutOnY = (dict) => {
  // dict: {x: list, y: list}, ex. {x: list1, y:ret}
  if (dict.y) {
    // not null
    //list1 = [1], ret = [7,8,9]
    // get who is the last element of ret
    var lastOfRet = getLastElementOfList(dict.y);
    lastOfRet.next = dict.x; //list1 = [1], ret = [7,8,9,1]
    dict.x = dict.x.next; //list1 = null, ret = [7,8,9,1]
    lastOfRet.next.next = null; //list1 = null, ret = [7,8,9,1]
  } else {
    //ret is null
    //list1 = [1,2,4], ret = []
    dict.y = dict.x; // list1 = [1,2,4], ret = [1,2,4]
    dict.x = dict.x.next; // list1 = [2,4], ret = [1,2,4], ret.next = [2,4]
    dict.y.next = null; // list1 = [2,4], ret = [1]
  }
  return dict;
};

var mergeTwoLists = function (list1, list2) {
  var ret = null; //new ListNode(null,null);

  // while list1 or list2 have elements? yes
  while (list1 || list2) {

    //   list2 have elements? yes
    if (list2 && list1) {
      //     is the 1st element of list1 < 1st element of list2?
      if (list1.val < list2.val) {
        //       yes then: grab the 1st element of list1 and put on ret
        var dict = grab1stElemOfXAndPutOnY({ x: list1, y: ret });
        list1 = dict.x;
        ret = dict.y;
      } else {
        //       no (list2) then: grab the 1st element of list2 and put on ret
        var dict = grab1stElemOfXAndPutOnY({ x: list2, y: ret });
        list2 = dict.x;
        ret = dict.y;
      }
    } else if (!list2) {
      //     list 2 have no elements:
      //       then: grab the list1 and put on ret
      if (ret) {
        getLastElementOfList(ret).next = list1;
      } else {
        ret = list1;
      }
      list1 = null;
    } else if (!list1) {
      //     list 1 have no elements:
      //       then: grab the 1st element of list2 and put on ret
      if (ret) {
        getLastElementOfList(ret).next = list2;
      } else {
        ret = list2;
      }
      list2 = null;
    } // else is impossible

  }
  return ret
};

console.log("Ex 1")
console.log(JSON.stringify(mergeTwoLists(list1, list2)));


console.log("Ex 2");
console.log(JSON.stringify(mergeTwoLists(null,null)));


console.log("Ex 3");
console.log(JSON.stringify(mergeTwoLists(null, new ListNode(0, null))));
