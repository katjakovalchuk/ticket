"""
Linked Queue implementation.
"""


class Queue:
    """
    Linked queue implementation.
    """

    # Private storage class for creating the linked list nodes.
    class _QueueNode:
        """
        Queue node.
        """

        def __init__(self, item):
            """
            Standart func in class
            """
            self.item = item
            self.next = None

    def __init__(self):
        """
        Standart func in class
        """
        self._qhead = None
        self._qtail = None
        self._count = 0

    # Returns True if the queue is empty.
    def isEmpty(self):
        """
        Returns True if the queue is empty.
        """
        return self._qhead is None

    # Returns the number of items in the queue.
    def __len__(self):
        """
        Returns the number of items in the queue.
        """
        return self._count

    # Adds the given item to the queue.
    def enqueue(self, item):
        """
        Adds the given item ti the queue
        """
        node = self._QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue(self):
        """
        Removes and returns the first item in the queue.
        """
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None

        self._qhead = self._qhead.next
        self._count -= 1
        return node.item
