"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Deev Patel
ID:     169032799
Email:  pate2799@mylaurier.ca
__updated__ = "2022-09-14"
------------------------------------------------------------------------
"""
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque


deque = Deque()
array = [10, 6, 4, 5, 3, 8, 9, 2, 1, 7]
for i in array:
    deque.insert_front(i)

print ("Original Deque:")
for i in deque:
    print (i)

Sorts.gnome_sort(deque)

print ("After Gnome Sort:")

for i in deque:
    print (i)