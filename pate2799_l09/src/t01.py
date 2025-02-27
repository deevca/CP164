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
from functions import hash_table
from Movie_utilities import read_movies

fv = open('movies.txt', 'r')

a = read_movies(fv)
hash_table(5, a)

fv.close()