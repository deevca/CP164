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
from Movie_utilities import get_by_rating, read_movies

name = "movies.txt"
fh = open(name, 'r')


rmovies = get_by_rating(read_movies(fh), 6.7)

for i in range(len(rmovies)):
    print(rmovies[i])
    print()

fh.close()