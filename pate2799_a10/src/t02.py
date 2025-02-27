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
from Sorts_List_linked import Sorts
from List_linked import List

array = List()
array.append(0)
array.append(0)
array.append(0)


Sorts.radix_sort(array)

for v in array:
    print(v)