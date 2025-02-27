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
from Sorted_List_linked import Sorted_List
from Movie_utilities import read_movies
from utilities import list_test
# Constants

fh = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fh)

list_test(movies)