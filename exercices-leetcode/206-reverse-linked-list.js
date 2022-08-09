/*
Given the head of a singly linked list, reverse the list, and return the reversed list.


head  next                       null
[1] -> [2] -> [3] -> [4] -> [5]
p1      p2

output
[5] -> [4] -> [3] -> [2] -> [1]
*/

 // Definition for singly-linked list.
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

var reverseList = function (head) {
    let [prev, current, next] = [null, head, null];
    while (current) {
      // salva
      next = current.next;
      // inverte
      current.next = prev;
      // avança para o proximo
      prev = current;
      current = next;
    }
    return prev;
};

const list = [1, 2, 3, 4, 5];

console.log(reverseList(list));
