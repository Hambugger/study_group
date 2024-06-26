
from queue import Empty


class ListStack:
    """ LIFO Stack implement using singly linked list list for storage."""

    # _______ Nested class_________

class _Node:
    """ Lightweight, nonpublic class for storing a singly linked list node. """
    __slots__ = '_element','_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

# -----------------stack methods---------------

def __init__(self):
    """ Create an empty stack."""
    self._head = None
    self._size = 0

def __len__(self):
    """ Return the number of elements in the stack. """
    return self._size

def is_empty(self):
    """ Return true if the stack is empty."""
    return self._size == 0

def push(self, e):
    """ Add element e to te top of the stack. """
    self._head =self._Node(e, self._head)
    self._size += 1

def top(self):
    """ return (but do not remove ) the element at the top of the stack.
    Raise an error Empty exception """
    if self.is_empty():
        raise Empty('The stack is empty')
    return self._head._element

def pop(self):
    """ Remove and return the element from the top of the stack (i.e LIFO).
    Raise Empty exception if the stack is empty."""
    if self.is_empty():
        raise Empty('stack is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    return answer
    
