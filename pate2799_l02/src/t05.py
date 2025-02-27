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
from utilities import stack_test

fv = open("movies.txt", "r")
l = []

for line in fv:
    l.append(line)

stack_test(l)

fv.close()