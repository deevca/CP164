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
from List_array import List

source = List()

source.append(5)
source.append(6)
source.insert(0, 4)

n = source.index(5)
print(n)

value = source.find(4)
print(value)

n = source.count(6)
print(n)

value = source.min()
print(value)

value = source.max()
print(value)