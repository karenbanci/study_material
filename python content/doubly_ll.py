# pylint: disable=raise-missing-from
"""
Final Project: Doubly Linked List
By Karen Banci, 2023

Link of the final project:
https://docs.google.com/document/d/1C5MgdHC03-euac_3-8UJ0v3Yhf2gAD_0nwN6WhBc62w/edit?usp=sharing
"""


class DoublyLinkedListNode:
    """
    This class represents a node in a doubly linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    @property
    def data(self):
        """
        Getter for data
        """
        return self._data

    @data.setter
    def data(self, new_data):
        """
        Setter for data
        """
        self._data = new_data

    @property
    def next(self):
        """
        Getter for next
        """
        return self._next

    @next.setter
    def next(self, new_next):
        """
        Setter for next
        """
        self._next = new_next

    @property
    def previous(self):
        """
        Getter for previous
        """
        return self._previous

    @previous.setter
    def previous(self, new_previous):
        """
        Setter for previous
        """
        self._previous = new_previous

    def __str__(self):
        return f"{self._data}"

    def __repr__(self):
        return (f"new_data={self._data}, "
                f"next={id(self._next)}, "
                f"previous={id(self._previous)}")


class DoublyLinkedList:
    """
    This class represents a doubly linked list
    """
    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._size = 0

        if iterable is not None:
            try:
                iterable = reversed(iterable)
            except TypeError:
                pass
            for i in iterable:
                self.add_to_head(i)

    @property
    def size(self):
        """
        Getter for size
        """
        return self._size

    def __len__(self):
        return self.size

    def add_to_head(self, data):  # O(1) - constant time
        """
        Add a new node to the head of the list
        @param data: the data to be added to the head
        """
        node = DoublyLinkedListNode(data)
        node.next = self._head
        if self._head is not None:
            self._head.previous = node
        self._head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def add_to_tail(self, data):  # O(1) - constant time
        """
        Add a new node to the tail of the list
        @param data: the data to be added to the tail
        """
        node = DoublyLinkedListNode(data)
        if self._tail is not None:
            self._tail.next = node
            node.previous = self._tail
        self._tail = node
        if self._head is None:
            self._head = node
        self._size += 1

    def insert(self, index, data):
        """
        Insert a new node at a specific index
        @param index: the index to insert the new node
        @param data: the data to be inserted

        """
        try:
            if index == 0:
                self.add_to_head(data)  # O(1) - constant time
            elif index == self.size:
                self.add_to_tail(data)  # O(1) - constant time
            else:
                curr = self._head
                while index != 0: # O(n) - linear time
                    curr = curr.next
                    index -= 1
                node = DoublyLinkedListNode(data) # O(1) - constant time
                node.next = curr
                node.previous = curr.previous
                curr.previous.next = node
                curr.previous = node
            self._size += 1

        except AttributeError:
            raise IndexError(f"index {index} is invalid")

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        return (f"\nsize={self._size}"
                f"\nhead={self._head}"
                f"\ntail={self._tail}"
                f"\nDDL = {[i for i in self]}")

    def _find_node(self, data): # O(n) - linear time
        """
        This method is used to find a node with a specific data and it does a
        validation check to see if the data is in the list
        """
        current = self._head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        raise KeyError(f"{data=} not found")

    def find(self, data): # O(n) - linear time
        """
        This method is used to find a node with a specific data and it raises
        the KeyError if the data is not in the list
        """
        for d in self:
            if d == data:
                return d
        raise KeyError(f"{data=} not found")

    def remove(self, data): # O(n) - linear time
        """
        This method is used to remove a node with a specific data
        """
        curr_node = self._find_node(data)
        try:
            if curr_node.data == data:
                if curr_node.data == self._head.data:
                    self._head = curr_node.next
                    self._head.previous = None

                elif curr_node.data == self._tail.data:
                    self._tail = curr_node.previous
                    self._tail.next = None

                else:
                    previous = curr_node.previous
                    next = curr_node.next

                    previous.next = next
                    next.previous = previous

                self._size -= 1

        except KeyError:
            return f"{data=} was not found"

    def __getitem__(self, index):
        """
        Get the data at a specific index
        """
        self._validate_index(index)
        curr = self._head
        while index != 0:
            curr = curr.next
            index -= 1
        return curr.data

    def __setitem__(self, index, new_data):
        """
        Set the data to a new data at a specific index
        """
        self._validate_index(index)
        curr = self._head
        while index != 0:
            curr = curr.next
            index -= 1
        curr.data = new_data

    def __contains__(self, item):
        """
        Returns True if item is in the list, False otherwise
        """
        for i in self:
            if i == item:
                return True
        return False

    def _validate_index(self, index):
        """
        Validate the index to make sure it is an integer and within the range
        of the list
        """
        if not isinstance(index, int):
            raise TypeError("index should be int")

        if index < 0 or index >= self.size:
            raise ValueError(f"index {index} is invalid")
