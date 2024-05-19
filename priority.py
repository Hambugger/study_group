class PriorityQueueBase:
    """ Abstract base class for a priority queue. """
    class _item:
        """ Lightweight composite to store priority queue itmes. """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        """ return True if the priority queue is Empty. """
        return len(self) == 0
