class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next_node
    
class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._length = 0
        # Initialize in normal order
        for value in values:
            self.push(value)

    def __len__(self):
        count = 0
        node = self._head
        while node:
            count += 1
            node = node.next()
        return count

    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        new_node = Node(value, self._head)
        self._head = new_node
        self._length += 1

    def pop(self):
        if self._length == 0:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        self._length -= 1
        return value

    def reversed(self):
        return LinkedList(list(self))

    def __iter__(self):
        node = self._head
        while node:
            yield node.value()
            node = node.next()
            
class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
    pass



