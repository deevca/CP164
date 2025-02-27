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
from utilities import array_to_queue
# Constants

source = Queue()
target = Queue()

source_arr = [1, 2, 3, 4, 5]
target_arr = [5, 4, 3, 2, 1]

array_to_queue(source, source_arr)
array_to_queue(target, target_arr)

print(f'source queue: {source._values}')
print(f'target queue: {target._values}')

equals = (source == target)
print(f'equal queues: {equals}')