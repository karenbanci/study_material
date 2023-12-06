"""
Final Project: Doubly Linked List Test
"""

import unittest
from random import random

from doubly_ll import *


class LinkedListTestCase(unittest.TestCase):
    def testInit(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll._head, None)
        self.assertEqual(dll._tail, None)
        self.assertEqual(dll.size, 0)

    def testInitWithIterable(self):
        dll = DoublyLinkedList([1, 2, 3, 4, 5])
        self.assertEqual(dll._head.data, 1)
        self.assertEqual(dll._tail.data, 5)
        self.assertEqual(dll._head.next.data, 2)
        self.assertEqual(dll.size, 5)

    def testAddToHead(self):
        dll = DoublyLinkedList()

        for d in range(20):
            dll.add_to_head(d)

        print(dll)

        self.assertEqual(dll._tail.data, 0)
        self.assertEqual(dll._tail.previous.data, 1)
        self.assertEqual(dll._head.data, 19)
        self.assertEqual(dll._head.next.data, 18)
        self.assertIsNone(dll._head.previous)
        self.assertIsNone(dll._tail.next)

    def testAddToTail(self):
        dll = DoublyLinkedList()
        dll.add_to_tail(1)
        print(dll)

        dll.add_to_tail(2)
        print(dll)

        dll.add_to_tail(3)
        print(dll)

        self.assertEqual(dll.size, 3)
        self.assertEqual(dll._head.data, 1)
        self.assertEqual(dll._tail.data, 3)
        self.assertEqual(dll._head.next.data, 2)
        self.assertEqual(dll._head.previous, None)
        self.assertEqual(dll._tail.previous.data, 2)
        self.assertEqual(dll._tail.next, None)
        self.assertEqual(dll._head.next.next.data, 3)

    def testInsertNode(self):
        dll = DoublyLinkedList(['John', 'Amanda', 'Anna', 'Maria', 'Luke'])

        dll.insert(2, 'Sophia')
        self.assertEqual(dll.size, 6)
        print(dll)

        dll.insert(5, 'Peter')
        self.assertEqual(dll.size, 7)
        print(dll)

    def testInsertNodeIndexInvalid(self):
        dll = DoublyLinkedList(['John', 'Amanda', 'Anna', 'Maria', 'Luke'])
        with self.assertRaises(IndexError):
            dll.insert(10, 'Sophia')

    def testFindData(self):
        dll = DoublyLinkedList()
        data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        for d in data:
            dll.add_to_head(d)

        dll.find("e")
        self.assertEqual(dll.find('e'), 'e')

    def testFindDataInvalid(self):
        dll = DoublyLinkedList()
        data = ['Jenny', 'Zibin ', 'Josh', 'Mark', 'Luke']

        for d in data:
            dll.add_to_head(d)

        with self.assertRaises(KeyError):
            dll.find('Peter')

    def testRemoveHeadNode(self):
        dll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        print(dll)
        dll.remove('a')
        print(dll)

        self.assertEqual(dll._head.data, 'b')
        self.assertEqual(dll._head.previous, None)
        self.assertEqual(dll._head.next.data, 'c')
        self.assertEqual(dll.size, 8)

    def testRemoveTailNode(self):
        dll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        print(dll)
        dll.remove('i')
        print(dll)
        self.assertEqual(dll._tail.data, 'h')
        self.assertEqual(dll._tail.previous.data, 'g')
        self.assertEqual(dll._tail.next, None)
        self.assertEqual(dll.size, 8)

    def testRemoveMiddleNode(self):
        dll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        print(dll)
        dll.remove('e')
        print(dll)
        self.assertEqual(dll._head.next.next.next.next.data, 'f')
        self.assertEqual(dll._head.next.next.next.next.previous.data, 'd')
        self.assertEqual(dll.size, 8)

    def testRemoveNodeInvalid(self):
        dll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        with self.assertRaises(KeyError):
            dll.remove('k')

    def testSetItem(self):
        dll = DoublyLinkedList(['John', 'Amanda', 'Anna', 'Maria', 'Luke'])
        print(dll)
        dll[0] = 'Peter'
        print(dll)
        self.assertEqual(dll._head.data, 'Peter')
        self.assertEqual(dll._head.next.data, 'Amanda')
        self.assertEqual(dll._head.next.previous.data, 'Peter')
        self.assertEqual(dll.size, 5)

    def testInsertThousandItems(self):
        dll = DoublyLinkedList()
        for i in range(1000):
            dll.add_to_tail(i)
        self.assertEqual(dll.size, 1000)
        self.assertEqual(dll._head.data, 0)
        self.assertEqual(dll._tail.data, 999)
        self.assertEqual(dll._head.next.data, 1)
        self.assertEqual(dll._head.next.previous.data, 0)
        self.assertEqual(dll._tail.previous.data, 998)
        self.assertEqual(dll._tail.previous.next.data, 999)
        self.assertEqual(dll._tail.next, None)
        self.assertEqual(dll._head.previous, None)

    def testContains(self):
        dll = DoublyLinkedList()
        for i in range(1000):
            dll.add_to_tail(i)
        self.assertTrue(999 in dll)
        self.assertFalse(1200 in dll)
