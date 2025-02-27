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
from Movie_utilities import get_by_year, read_movies
name = "movies.txt"

fh = open(name, 'r')


ymovies = get_by_year(read_movies(fh), 1977)

for i in range(len(ymovies)):
    print(ymovies[i])
    print()


fh.close()