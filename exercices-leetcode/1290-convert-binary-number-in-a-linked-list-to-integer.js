/*
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0
*/

// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {number}
 */
const getDecimalValue = (head) => {
  let val = 0;
  while (head) {
    // First, the << operation means to move to left by n bit in the binary representation.
    //Then, the | operation has almost the same logic as || but it's for bit manipulation.
    val = (val << 1) | head.val;
    head = head.next;
  }
  return val;
};



const head = new ListNode(1, new ListNode(0, new ListNode(1, null)));
console.log(getDecimalValue(head));

//explanation https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/461356/JavaScript-Easy-to-understand-bit-operator


 /*
Runtime: 105 ms, faster than 20.07% of JavaScript online submissions for Convert Binary Number in a Linked List to Integer.

Memory Usage: 42.2 MB, less than 27.35% of JavaScript online submissions for Convert Binary Number in a Linked List to Integer.

*/
