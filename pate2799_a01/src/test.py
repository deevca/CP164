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
char = input("Enter character: ")

if char.isupper():
    print(f"{char} is an uppercase character.")
elif char.islower():
    print(f"{char} is a lowercase character.")
else:
    print(f"{char} is not a letter.")