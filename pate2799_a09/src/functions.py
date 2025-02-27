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
# Imports
from Word import Word

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    for v in fv:
        word = ''
        for letter in v:
            if letter.isalpha():
                word += letter.lower()
            else:
                if len(word) > 0:
                    wrd = Word(word)
                    hash_set.insert(wrd)
                word = ''
    return

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    max_word = ''
    max_word_count = 0
    total = 0
    for v in hash_set:
        total += v.comparisons
        if v.comparisons > max_word_count:
            max_word = v
            
    return total, max_word