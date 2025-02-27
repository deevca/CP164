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
from functions import pq_split_key

key = 5
source = Priority_Queue()
source.insert(10)
source.insert(1)
source.insert(5)
source.insert(25)
source.insert(0)
print(f'source: {source._values}')
print(f'key: {key}')

target1 = Priority_Queue()
target2 = Priority_Queue()

target1, target2 = pq_split_key(source, key)
print(f'target1: {target1._values}')
print(f'target2: {target2._values}')