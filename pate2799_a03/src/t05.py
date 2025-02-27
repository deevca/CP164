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
from Stack_array import Stack
from functions import is_palindrome_stack


stack = Stack()
string = str(input("Enter the string: "))
        
palindrome = is_palindrome_stack(string)

print (palindrome)