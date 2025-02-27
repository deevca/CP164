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
# Imports
from List_linked import List
list = List()

# Append Function
list.append(1), list.append(5), list.append(77)
for i in list:
    print(i)
print()

# Prepend Function (should go to the front)
list.prepend(55)
for i in list:
    print(i)
print()

# Insert Function
list.insert(-1, 33)
for i in list:
    print(i)