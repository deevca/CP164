"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from Sorted_List_array import Sorted_List
# Define the new_slot slot creation function.
new_slot = Sorted_List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size slots.
        Use: hs = Hash_Set(slots)
        -------------------------------------------------------
        Parameter:
            slots - number of initial slots in Hash Set (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        self._count = 0

        # Define the empty slots.
        for _ in range(self._slots):
            self._table.append(new_slot())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """

        # your code here

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        inserted = False
        h = hash(value)
        slot = h % self._slots

        found = False
        i = 0
        while i < len(self._table[slot]) and not found:
            if self._table[slot][i] == value:
                found = True
            i += 1

        if not found:
            self._table[slot].insert(value)
            inserted = True

        if inserted:
            self._count += 1
        if self._count > self._LOAD_FACTOR * self._slots:
            self._rehash()
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here

        return

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        value = None
        h = hash(key)
        slot = h % self._slots

        found = False
        i = 0
        while i < len(self._table[slot]) and not found:
            if self._table[slot][i] == key:
                found = True
            else:
                i += 1
        if found:
            value = self._table[slot].pop(i)

        if value is not None:
            self._count -= 1
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        old_slots = self._slots
        self._slots = 2 * self._slots + 1
        new_slots = self._slots - old_slots
        for _ in range(new_slots):
            self._table.append(new_slot())
        i = 0

        while i < old_slots:
            j = 0
            while j < len(self._table[i]):
                value = self._table[i].pop(j)
                h = hash(value)
                slot = h % self._slots
                self._table[slot].insert(value)
                j += 1
            i += 1
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values 
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        print('{} slots'.format(self._slots))
        print()
        while i < len(self._table):
            print(SEP)
            print('Slot {}'.format(i))
            print()
            j = 0
            while j < len(self._table[i]):
                print(self._table[i][j])
                print()
                j += 1
            i += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item