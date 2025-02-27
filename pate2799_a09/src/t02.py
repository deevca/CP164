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
from Hash_Set_sorted import Hash_Set
from functions import insert_words,comparison_total

fn = "miserables.txt"
fv = open(fn, "r", encoding="utf-8")
hs = Hash_Set(20)

insert_words(fv,hs)
total,max_word = comparison_total(hs)
print("Using array-based Sorted List Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(max_word.word,max_word.comparisons))