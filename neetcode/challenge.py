#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# class SinglyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, node_data):
#         node = SinglyLinkedListNode(node_data)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node

#         self.tail = node

# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))

#         node = node.next

#         if node:
#             fptr.write(sep)



#
# Complete the 'deleteEven' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST listHead as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# def deleteEven(listHead):
#     # Write your code here
#     return [curr for curr in listHead if curr % 2 != 0]


# print(deleteEven([1, 2, 3, 4, 6]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     listHead_count = int(input().strip())

#     listHead = SinglyLinkedList()

#     for _ in range(listHead_count):
#         listHead_item = int(input().strip())
#         listHead.insert_node(listHead_item)

#     result = deleteEven(listHead.head)

#     print_singly_linked_list(result, '\n', fptr)
#     fptr.write('\n')

#     fptr.close()

#!/bin/python3

#
# Complete the 'maximumOccurringCharacter' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.
#

# def maximumOccurringCharacter(text):
#     # Write your code here
#     # Dicionário para armazenar a contagem de cada caractere
#     char_count = {}

#     # Iterar sobre cada caractere no texto
#     for char in text:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     # Encontrar o caractere com a maior contagem
#     max_char = None
#     max_count = 0

#     for char, count in char_count.items():
#         if count > max_count:
#             max_count = count
#             max_char = char

#     return max_char


# print(maximumOccurringCharacter("abbbaacc"))
