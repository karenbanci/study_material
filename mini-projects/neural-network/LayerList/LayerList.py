class DoublyLinkedList:
    """
    Note that the DoublyLinkedList class is a generic data type separate
     from any conversation about neural networks.
     For this class DoublyLinkedList, any mention of "nodes" refers to
     a linked list node, not to a neurode.
    """
    class EmptyListError(BaseException):
        pass

    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._curr = None

    def move_forward(self):
        """
        Move the current pointer forward one node.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.next is None:
            raise IndexError
        self._curr = self._curr.next

    def move_back(self):
        """
        Move the current pointer back one node.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.prev is None:
            raise IndexError
        self._curr = self._curr.prev

    def reset_to_head(self):
        """
        Reset the current pointer to the head of the list if the
        list is not empty.
        """
        if self._head is None:
            raise DoublyLinkedList.EmptyListError
        self._curr = self._head

    def reset_to_tail(self):
        """
        Reset the current pointer to the tail of the list if the
        list is not empty.
        """
        if self._tail is None:
            raise DoublyLinkedList.EmptyListError
        self._curr = self._tail

    def add_to_head(self, data):
        """
        Add a new node to the head of the list.
        If the list is empty, the new node should also be the tail
        of the list. In either case, the current pointer should be reset
        to the head of the list.
        """
        new_node = DoublyLinkedList.Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._curr = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
            self._curr = new_node

    def add_after_cur(self, data):
        """
        Add a new node after the current node.
        If the current node is the tail of the list,
        the new node should also be the tail of the list.
        In either case, the current pointer should not change
        """
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
        """
        Remove the node at the head of the list and return data.
        If the list is empty, raise an EmptyListError.
        If the list has only one node, the tail pointer should be set to None.
        In either case, the current pointer should be reset to the
        head of the list.
        """
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
        """
        If the list is empty, raise an EmptyListError.
        If the current node is the tail of the list, raise an IndexError.
        If the current node is the second to last node,
        the tail pointer should be set to the current node.
        In either case, the current pointer should not change.
        Remove the node after the current node and return data.
        """
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
        """
        If the list is empty, raise an EmptyListError.
        Return the data at the current node.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        return self._curr.data


def dll_test():
    my_list = DoublyLinkedList()
    try:
        my_list.get_current_data()
    except DoublyLinkedList.EmptyListError:
        print("Pass")
    else:
        print("Fail")
    for a in range(3):
        my_list.add_to_head(a)
    if my_list.get_current_data() != 2:
        print("Error")
    my_list.move_forward()
    if my_list.get_current_data() != 1:
        print("Fail")
    my_list.move_forward()
    try:
        my_list.move_forward()
    except IndexError:
        print("Pass")
    else:
        print("Fail")
    if my_list.get_current_data() != 0:
        print("Fail")
    my_list.move_back()
    my_list.remove_after_cur()
    if my_list.get_current_data() != 1:
        print("Fail")
    my_list.move_back()
    if my_list.get_current_data() != 2:
        print("Fail")
    try:
        my_list.move_back()
    except IndexError:
        print("Pass")
    else:
        print("Fail")
    my_list.move_forward()
    if my_list.get_current_data() != 1:
        print("Fail")


dll_test()

"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/
Project CS_3B_Winter_2023/CS_3B_Winter_2023/LayerList/LayerList.py 

Pass
Pass
Pass

Process finished with exit code 0
"""