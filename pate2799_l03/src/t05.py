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
from Priority_Queue_array import Priority_Queue

queue = Priority_Queue()

qlist = [5, 4, 3, 10, 11]

for i in qlist:
    queue.insert(i)

for i in queue:
    print(i)


queue.remove()
print()

for i in queue:
    print(i)