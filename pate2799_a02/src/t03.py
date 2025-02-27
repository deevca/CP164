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
from Movie_utilities import get_by_genre, read_movies

name = "movies.txt"
fh = open(name, 'r')

gmovies = get_by_genre(read_movies(fh), 0)

for i in range(len(gmovies)):
    print(gmovies[i])
    print()
