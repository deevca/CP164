"""
-------------------------------------------------------
Array version of the Priority Queue Set ADT.
-------------------------------------------------------
Author: Deev Patel
ID:     169032799
Email:  pate2799@mylaurier.ca
__updated__ = "2023-06-20"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from copy import deepcopy


class Priority_Queue_Set:
    """
    Implements an array-based Priority Queue Set ADT.
    """

    def insert(self, value):
        """
        -------------------------------------------------------
        A unique copy of value is appended to the end of source,
        and _first is updated as appropriate to the index of
        value with the highest priority.
        Allows only one copy of value.
        Use: inserted = source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            inserted - True if value is inserted, False otherwise
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        # your code here
        if len(self._values) == 1:
            self._first = 0
            
        else:
            if value < self._values[self._first]:
                self._first = len(self._values) - 1

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines source1 and source2 into target.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Allows only one copy of value in target.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based Priority Queue Set (Priority_Queue_Set)
            source2 - an array-based Priority Queue Set (Priority_Queue_Set)
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            None
        -------------------------------------------------------
        """

        # your code here
        while len(source1._values) > 0 and len(source2._values) > 0:
            self._values.append(source1._values.pop(0))
            self._values.append(source2._values.pop(0))

        while len(source1._values) > 0:
            self._values.append(source1._values.pop(0))

        while len(source2._values) > 0:
            self._values.append(source2._values.pop(0))
        source1._first = None
        source2._first = None
        self._set_first()
        
        return
            

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Priority Queue Set.
        Use: source = Priority_Queue_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            a new Priority_Queue_Set object (Priority_Queue_Set)
        -------------------------------------------------------
        """
        self._values = []
        self._first = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            the number of values in source.
        -------------------------------------------------------
        """
        return len(self._values)

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper method to set the value of self._first.
        _first is the index of the value with the highest
        priority in self. None if self is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            None
        -------------------------------------------------------
        """
        n = len(self._values)

        if n == 0:
            self._first = None
        else:
            self._first = 0

            for i in range(1, n):
                if self._values[i] < self._values[self._first]:
                    self._first = i
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from source.
        Use: value = source.remove()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            value - the highest priority value in source -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(
            self._values) > 0, "Cannot remove from an empty Priority Queue Set"

        value = self._values.pop(self._first)
        # Find the value with the next highest priority.
        self._set_first()
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            value - a copy of the highest priority value in srouce -
                the value is not removed from source. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty Priority Queue Set"

        value = deepcopy(self._values[self._first])
        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
