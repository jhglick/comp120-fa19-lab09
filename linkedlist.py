# File: LinkedList.py
# Date: November 5, 2019
# Author: COMP 120 class
# Description: Contains recursive methods
#      to display a linked list, and reverse it.

class Node:
    """ Initialize the node """
    def __init__(self, item, next = None):
        self.item = item
        self.next = next
    
class LinkedList:
    def __init__(self):
        """ Initialize the linked list"""

        self.front = None

    def append_front(self, item):
        """ Append new item to front of linked list"""

        self.front = Node(item, self.front)

    def __str__(self):
        """ Return string representation of linked list"""

        return LinkedList.str_recursive(self.front)

    def str_reverse(self):
        """ Return string representation of reverse of the linked list"""

        return LinkedList.str_reverse_recur(self.front)
        
    @staticmethod
    def str_recursive(node):
        """ Return string representation of the sublist headed by node. """

        if node == None:
            return ""
        else:
            return str(node.item) + " " + LinkedList.str_recursive(node.next)

    @staticmethod
    def str_reverse_recur(node):
        """ Return string representation of the reverse of the sublist headed by node. """

        if node == None:
            return ""
        else:
            return LinkedList.str_reverse_recur(node.next) + " " + str(node.item)

    def reverse(self):
        """ Reverse the linked list. """

        (self.front, _) = LinkedList.reverse_recursive(self.front)

    @staticmethod
    def reverse_recursive(node):
        """ Reverse the sublist headed by node.  Return the front and
            back of the reversed list.
        """
        if node == None:
            return (None, None)
        elif node.next == None:
            return (node, node)
        else:
            (front, back) = LinkedList.reverse_recursive(node.next)
            back.next = node
            node.next = None
            return (front, node)

if __name__ == "__main__":
    l = LinkedList()
    l.append_front(4)
    l.append_front(3)
    l.append_front(2)
    l.append_front(1)

    print("Here is l: " + str(l))
    print("Here is the reverse of l: " + l.str_reverse())

    print("Now reversing l.")
    l.reverse()
    print("And here is l after it has been reversed:")
    print(l)
