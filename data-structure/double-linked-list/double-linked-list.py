"""
class DoublyLinkedList
Note that the DoublyLinkedList class is a generic data type separate from any conversation about neural networks.  For this class DoublyLinkedList, any mention of "nodes" refers to a linked list node, not to a neurode.

This class implements a doubly linked list as described in the lectures.  The data type you create must be in the spirit of a doubly linked list:

There must be a head node
There must be a tail node
Each node should point to its neighbors in the list
Most important: there must not be any kind of collection that contains all the nodes.  For example, this is not a doubly linked list if you use a Python list to contain all the nodes...even if the external behavior is the same.
You will need to create a class for the nodes, and an exception class DoublyLinkedList.EmptyListError

The constructor takes no arguments.

The following methods take no arguments (other than self) and simply move the current pointer over the linked list.  All of the methods should raise EmptyListError if the list is empty.  The first two should raise IndexError if they try to move beyond the end of the list.  Note: The code in the lectures allows the self._curr pointer to move off the end of the list, to None.  For this assignment please leave self._curr at the head or tail if a move would send it off the end of the list.

move_forward(self)
move_back(self)
reset_to_head(self)
reset_to_tail(self)
The following methods take one argument (data) and adds it to the list.  Remember that "adding data" to the list means creating a new linked list node, placing the data in the node, and placing the node into the correct place in the list.

add_to_head(self, data)
add_after_cur(self, data)
The following methods remove a node and return its data.  They should both raise an EmptyListError if the list is empty.  The second method should raise an IndexError if the current node is the tail.

remove_from_head(self)
remove_after_cur(self)
This method returns the data at the current node.  If the list is empty, raise an EmptyListError.

get_current_data(self)
"""

class DoublyLinkedList:
    class EmptyListError(Exception):
        pass

    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._curr = None

    def move_forward(self):
        '''Move the current pointer forward one node.  If the current pointer is at the tail of the list, raise an IndexError.  If the list is empty, raise an EmptyListError.'''
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.next is None:
            raise IndexError
        self._curr = self._curr.next

    def move_back(self):
        '''Move the current pointer back one node.  If the current pointer is at the head of the list, raise an IndexError.  If the list is empty, raise an EmptyListError.'''
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.prev is None:
            raise IndexError
        self._curr = self._curr.prev

    def reset_to_head(self):
        '''Reset the current pointer to the head of the list if the list is not empty.  If the list is empty, raise an EmptyListError.'''
        if self._head is None:
            raise DoublyLinkedList.EmptyListError
        self._curr = self._head

    def reset_to_tail(self):
        '''Reset the current pointer to the tail of the list if the list is not empty.  If the list is empty, raise an EmptyListError.'''
        if self._tail is None:
            raise DoublyLinkedList.EmptyListError
        self._curr = self._tail

    def add_to_head(self, data):
        '''Add a new node to the head of the list.  The new node should contain the data passed in as an argument.  If the list is empty, the new node should also be the tail of the list.  In either case, the current pointer should be reset to the head of the list.'''
        new_node = DoublyLinkedList.Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._curr = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    def add_after_cur(self, data):
        '''Add a new node after the current node.  The new node should contain the data passed in as an argument.  If the current node is the tail of the list, the new node should also be the tail of the list.  In either case, the current pointer should not change.'''
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError

        new_node = DoublyLinkedList.Node(data)

        if self._curr is self._tail:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        else:
            new_node.next = self._curr.next
            new_node.prev = self._curr
            self._curr.next.prev = new_node
            self._curr.next = new_node

    def remove_from_head(self):
        """Remove the node at the head of the list and return its data.  If the list is empty, raise an EmptyListError.  If the list has only one node, the tail pointer should be set to None.  In either case, the current pointer should be reset to the head of the list."""
        if self._head is None:
            raise DoublyLinkedList.EmptyListError
        if self._head is self._tail:
            data = self._head.data
            self._head = None
            self._tail = None
            self._curr = None
            return data
        else: # head is not tail
            data = self._head.data
            self._head = self._head.next
            self._head.prev = None
            self._curr = self._head
            return data

    def remove_after_cur(self):
        """Remove the node after the current node and return its data.  If the current node is the tail of the list, raise an IndexError.  If the list is empty, raise an EmptyListError.  If the current node is the second to last node, the tail pointer should be set to the current node.  In either case, the current pointer should not change."""
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr is self._tail:
            raise IndexError
        if self._curr.next is self._tail:
            data = self._tail.data
            self._tail = self._curr
            self._tail.next = None
            return data
        else: # curr.next is not tail
            data = self._curr.next.data
            self._curr.next = self._curr.next.next
            self._curr.next.prev = self._curr
            return data

    def get_current_data(self):
        """Return the data at the current node.  If the list is empty, raise an EmptyListError."""
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        return self._curr.data
