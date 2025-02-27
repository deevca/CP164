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
from functions import is_palindrome

string = input("Enter word: ")

palindrome = is_palindrome(string)

if palindrome:
    print(f"{string} is a palindrome")
else:
    print(f'{string} is not a palindrome')