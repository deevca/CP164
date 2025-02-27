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
from Movie_utilities import genre_counts, read_movies

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = genre_counts(movies)

print(ans)