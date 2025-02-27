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
from List_array import List
from Movie import Movie
from Movie_utilities import read_movie, read_movies
from utilities import array_to_list

# Prepare a List

file = open("movies.txt", "rt")

movies = read_movies(file)

file.close()

lst = List()

array_to_list(lst, movies)

source1.inset(4)
source1.insert(10)
source1.insert(6)

target1, target2 = source1.split_key(6)