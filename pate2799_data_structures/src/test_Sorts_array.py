"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
	from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []

    for i in range(SIZE):
        check = Number(i)
        values.append(check)

    return values

def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
	from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []

    for i in range(SIZE - 1, -1, -1):
        check = Number(i)
        values.append(check)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays = [[0 for x in range(SIZE)] for y in range(TESTS)]

    for i in range(TESTS):
        for a in range(SIZE):
            check = Number(random.randint(0, XRANGE))
            arrays[i][a] = check
    return arrays

def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    random = create_randoms()
    random_c = 0
    spacing = " " * (15 - len(title))

    Number.comparisons = 0
    Sorts.swaps = 0
   
    print(f"{title:>s}" , end='')
    func(create_sorted())
    sorted_c = Number.comparisons
    swaps_sorted = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    func(create_reversed())
    reversed_c = Number.comparisons
    swaps_reversed = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    for i in random:
        func(i)
        random_c += Number.comparisons
        Number.comparisons = 0
    random_c = random_c / len(random)
    swaps_random = Sorts.swaps / len(random)
    
    print(f"{spacing} {sorted_c:^8.0f} {reversed_c:^8.0f} {random_c:^8.0f} {swaps_sorted:^8.0f}         {swaps_reversed:^8.0f}         {swaps_random:>8.0f}")

    return
