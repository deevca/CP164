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
from utilities import array_to_queue

q1 = Queue()
q2 = Queue()

l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

array_to_queue(q1, l2)
array_to_queue(q2, l)

ns = queue_combine(q1, q2)

while not ans.is_empty():
    print(ans.remove())