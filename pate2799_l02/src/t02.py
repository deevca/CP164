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

stack = Stack()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")

stack.push(1)
value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("bottom")
stack.push("top")

print(stack.peek())
