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
from BST_linked import BST
from morse import encode_morse,fill_letter_bst, ByLetter
bst = BST()
text = "My name is Deev Patel."
data1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))
fill_letter_bst(bst, data1)

code = encode_morse(bst, text)
print("English: ")
print(text)
print("Morse code: ")
print(code)