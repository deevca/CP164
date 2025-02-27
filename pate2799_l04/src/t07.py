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
from utilities import list_test
from Movie import Movie

fv = open('movies.txt', 'r')

source = fv.readlines()

list_test(source)