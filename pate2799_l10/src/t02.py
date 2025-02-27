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
from test_Sorts_array import test_sort, SORTS

# Code
print ("Title             Sorted   Reversed Random    Swaps_sorted    Swaps_reversed     Swaps_random   ")
print ("")
for i in SORTS:
    test_sort(i[0], i[1])