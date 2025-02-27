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
from Hash_Set_array import Hash_Set

hs = Hash_Set(7)
ht = Hash_Set(7)
ht.insert(55)
hs.insert(55)
print(hs.is_identical(ht))