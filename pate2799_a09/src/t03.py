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
from functions import comparison_total, insert_words
from Hash_Set_BST import Hash_Set

# Code
fv = open("miserables.txt", "r")
hs = Hash_Set(20)
insert_words(fv, hs)

total, max_word = comparison_total(hs)

print ("Using linked BST Hash_set")
print ("")
print (f"Total Comparisons: {total}")
print (f"Word with maximum comparisons: {max_word}")