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
from utilities import array_to_stack
from Stack_array import Stack


stack = Stack()
source = [-1, -3, 14, -87, 9, 11]


array_to_stack(stack, source)

for i in stack:
    print(i)
