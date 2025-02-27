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
from Movie_utilities import get_by_genres, read_movies

genres = [3, 4]

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = get_by_genres(movies, genres)

for i in ans:
    print(i)

fv.close()