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
from Deque_linked import Deque

d = Deque()
for i in range(5):
    d.insert_front(i)

for j in d:
    print(i, end=" ")