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
r = source.remove(5)

print(r)
for i in source:
    print(i)