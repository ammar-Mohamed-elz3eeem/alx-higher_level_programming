#!/usr/bin/python3
"""
    Module singly_linked_list: Class for making nodes for SinglyLinkedList
"""


class Node:
    """
    Class Node: Class for making nodes for SinglyLinkedList
    """
    def __init__(self, num, next_node=None):
        self.data = num
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        if not isinstance(val, int):
            raise TypeError("data must be an integer")
        self.__data = val

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next):
        if next is None or isinstance(next, Node):
            self.__next_node = next
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglylinkedList Class"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, val):
        node = Node(val)
        if (self.__head is None):
            node.next_node = None
            self.__head = node
        elif (self.__head.data > val):
            node.next_node = self.__head
            self.__head = node
        else:
            list = self.__head
            while list.next_node is not None and list.next_node.data < val:
                list = list.next_node
            node.next_node = list.next_node
            list.next_node = node

    def __str__(self):
        data = []
        list = self.__head
        while list is not None:
            data.append(str(list.data))
            list = list.next_node
        return ('\n'.join(data))
