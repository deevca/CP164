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

bst = BST()
bst.insert(13)
bst.insert(18)
bst.insert(15)
bst.insert(31)
bst.insert(12)
bst.insert(20)
bst.insert(103)

zero, one, two = bst.node_counts()
print(zero, one, two)

print(13 in bst)

print(bst.parent(18))
print(bst.parent(20))