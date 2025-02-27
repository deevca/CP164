"""
-------------------------------------------------------
Simple midterm testing
-------------------------------------------------------
Author: Deev Patel
ID:     169032799
Email:  pate2799@mylaurier.ca
__updated__ = "2023-06-20"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from List_array import List
from Priority_Queue_Set_array import Priority_Queue_Set
from Queue_array import Queue
from functions import list_spin, thread_packets

# Constants
SEP = "-" * 60
SIZE = 6
VALUES = [4, 3, 5, 0, 2, 1]


def test_list_spin():
    """
    Tests list_spin function.
    """
    print(SEP)
    print("Testing 'list_spin'")
    print()
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    values = list(range(SIZE))

    for case in CASES:
        source = List()

        for value in values:
            source.append(value)
        print(f"source._values: {source._values}")
        list_spin(source, case)
        print(f"list_spin(source, {case})")
        print(f"source._values: {source._values}")
        print()
    return


def test_spin():
    """
    Tests spin method.
    """
    print(SEP)
    print("Testing 'spin'")
    print()
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    values = list(range(SIZE))

    for case in CASES:
        source = List()

        for value in values:
            source.append(value)
        print(f"source._values: {source._values}")
        source.spin(case)
        print(f"source.spin({case})")
        print(f"source._values: {source._values}")
        print()
    return


def test_pairwise_swap():
    """
    Tests pairwise_swap method.
    """
    print(SEP)
    print("Testing 'pairwise_swap'")
    print()
    CASES = (
        list(range(SIZE)),
        list(range(SIZE+1)),
    )
    for case in CASES:
        source = List()

        for value in case:
            source.append(value)
        print(f"source._values: {source._values}")
        source.pairwise_swap()
        print("source.pairwise_swap()")
        print(f"source._values: {source._values}")
        print()
    return


def print_set(name, source):
    """
    Prints Priority_Queue_Set formatted as 'name: [contents], _first'
    """
    print(f"{name}: {source._values}, {source._first}")
    return


def fill_set(values):
    """
    Fills a Priority_Queue_Set with contents of values
    """
    source = Priority_Queue_Set()
    for value in values:
        source.insert(value)
    return source


def test_insert():
    """
    Tests the Priority_Queue_Set insert method.
    """
    print(SEP)
    print("Test Priority_Queue_Set insert()")
    print()
    source = Priority_Queue_Set()
    print(f"Attempt to insert {VALUES} to source:")
    for value in VALUES:
        inserted = source.insert(value)
        print(f"inserted {value}: {inserted}")
    print_set("source", source)
    print()
    print("Test insert() with repeated values")
    print(f"Attempt to insert {VALUES} to source again:")
    for value in VALUES:
        inserted = source.insert(value)
        print(f"inserted {value}: {inserted}")
    print_set("source", source)
    print()


def test_combine():
    """
    Tests the Priority_Queue_Set combine method.
    """
    print(SEP)
    print("Test Priority_Queue_Set combine")
    print()
    source1 = fill_set(VALUES)
    print_set("source1", source1)
    source2 = fill_set(VALUES)
    print_set("source2", source2)
    target = Priority_Queue_Set()
    target.combine(source1, source2)
    print_set("source1", source1)
    print_set("source2", source2)
    print_set("target", target)
    print()


def test_thread_packets():
    """
    Tests thread_packets function.
    """
    print(SEP)
    print("Testing 'thread_packets'")
    print()
    CASES = (
        [[1, 2, 3, 4]],
        [[1, 3, 6], [2, 4, 5]],
        [[1, 3, 9], [2, 5, 6, 8], [4, 7, 10]],
    )
    for case in CASES:
        threads = []
        i = 0

        for values in case:
            queue = Queue()
            queue._values = values
            print(f"threads[{i}]._values: {queue._values}")
            threads.append(queue)
            i += 1

        packets = thread_packets(threads)
        print(f"packets._values: {packets._values}")
        print()
    return


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Midterm Testing")
    print()
    test_list_spin()
    test_spin()
    test_pairwise_swap()
    test_insert()
    test_combine()
    test_thread_packets()
