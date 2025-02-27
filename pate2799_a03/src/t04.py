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

source = Stack()
n = 5

for i in range(n):
    value = int(input("Enter a value: "))
    source.push(value)
    
print ("-------------")
print ("Unreversed Stack:")
for i in source:
    print (i)
source.reverse()

print ("-------------")
print ("Reversed Stack:")
for i in source:
    print (i)