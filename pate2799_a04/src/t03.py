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
from Queue_array import Queue
from functions import queue_combine

source1 = Queue()
source1.insert(5)
source1.insert(8)

source2 = Queue()
source2.insert(7)
source2.insert(9)
source2.insert(14)
print(f'Source1: {source1._values}')
print(f'Source2: {source2._values}')

target = queue_combine(source1, source2)

print(f'Target: {target._values}')