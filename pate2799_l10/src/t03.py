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
from test_Sorts_array import test_sort, SORTS, SIZE

# Code
print (f"n:    {SIZE}         |       Comparisons     |   |                 Swap                  |")
print ("Algorithm         In Order Reversed Random    In Order        Reveres            Random")

print ("--------------    -------- -------  --------  --------        --------         --------")

for i in SORTS:
    title = i[0]
    func = i[1]
    test_sort(title, func)