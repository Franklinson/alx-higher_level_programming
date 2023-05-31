#!/usr/bin/python3

"""Define a class called singly linked list"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a node with the given data and next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.
        """
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The value to be set as the data.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list with a head node."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (in increasing order).

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list."""
        current = self.head
        list_str = ""
        while current is not None:
            list_str += str(current.data) + "\n"
            current = current.next_node
        return list_str
