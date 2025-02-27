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
from Stack_array import Stack
from functions import stack_split_alt

s = Stack()
l = [4, 6, 8, 10, 11, 13, 7]

for i in l:
    s.push(i)
    
a1, a2 = stack_split_alt(s)

for i in a1:
    print(i)
    
print("*"*60)

for i in a2:
    print(i)