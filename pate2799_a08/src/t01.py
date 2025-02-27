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
bst.insert(5)
bst.insert(6)
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(8)


'''
print(tree.is_valid())
tree._root._right._value = 4
print(tree.is_valid())
'''
'''
tree2 = BST()
for i in range(1,7):
    tree2.insert(i)
'''
print(bst.levelorder())
bst.remove(3)
print(bst.levelorder())