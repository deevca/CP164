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
from utilities import array_to_list
from utilities import list_to_array

llist = List()
source = [4, 5, 6]
target = []

array_to_list(llist, source)

for i in llist:
    print(i)

list_to_array(llist, target)
print(target)