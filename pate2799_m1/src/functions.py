"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author: Deev Patel
ID:     169032799
Email:  pate2799@mylaurier.ca
__updated__ = "2023-06-20"
-------------------------------------------------------
"""
from tkinter.constants import END


def list_spin(source, n):
    """
    -------------------------------------------------------
    Rotates position of elements in source by n positions to the left.
    Use: source.spin(n)
    Use: list_spin(source, n)
    -------------------------------------------------------
    Parameters:
        source - the List to rotate (List)
        n - amount to rotate contents of List (int)
    Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
        None
    -------------------------------------------------------
    Examples:
        source: [0, 1, 2, 3, 4, 5], list_spin(source, 3), source: [3, 4, 5, 0, 1, 2]
        source: [0, 1, 2, 3, 4, 5], list_spin(source, -1), source: [5, 0, 1, 2, 3, 4]
    -------------------------------------------------------
    """
    # Your code here
    length = len(source)
    n = n % length 
    
    if n < 0:
        n += length
    
    else: 
        for i in range(n):
            val = source.pop(0)
            source.append(val)
            
    return


def thread_packets(threads):
    """
    -------------------------------------------------------
    Combines multiple queues into one queue where values
    in resulting queue are in order from minimum to maximum.
    Use: packets = thread_packets(threads)
    -------------------------------------------------------
    Parameters:
        threads - a list of queues to process (list of Queue)
    Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌​​​‌​‌‌‌‌‌:
        packets - a Queue (Queue)
    -------------------------------------------------------
    """

    # Your code here
    queue1 = threads[0]
    queue2 = threads[1]
    result = []

    if queue1 == [] and queue2 != []:
            result += queue2

    elif queue2 == [] and queue1 != []:
            result += queue1

    return result
