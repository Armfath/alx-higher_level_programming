#!/usr/bin/python3
"""
This module contain classes definition
"""


class Node:
    """
    Define a Node
    """
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

        if (type(next_node) == Node or (next_node is None)):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """
        data getter
        """

        return (self.__data)

    @property
    def next_node(self):
        """
        next_node getter
        """

        return (self.__next_node)

    @data.setter
    def data(self, value):
        """
        data setter
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter
        """

        if (type(value) == Node or (value is None)):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def __str__(self):
        return ("\n")
    def sorted_insert(self, value):
        new_node = Node(value)
    
            
    
        
    
