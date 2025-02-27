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
from Movie import Movie
from Movie_utilities import read_movies, get_movie, read_genres

fv = open("movies.txt", 'r')
movies = read_movies(fv)

for v in movies:
    print(v)
    
genres = read_genres()

movie = get_movie()

fv.close()