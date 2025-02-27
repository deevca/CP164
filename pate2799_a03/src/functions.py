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

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    i = 0

    while not source.is_empty():

        if i % 2 == 0:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        i += 1

    return target1, target2

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list = []
    for i in source:
        x = source.pop()
        list.append(x)
    for i in list:
        source.push(i) 

    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    cleaned = ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stack = Stack()
    palindrome = True
    n = 0
    x = 0
    for i in string:
        if i in letters:
            cleaned += i.lower()  
     
    while x < len(cleaned):
        stack.push(cleaned[x])        
        x += 1
        
    while palindrome == True and stack.is_empty() == False:   
        if stack.pop() != cleaned[n]:
            palindrome = False
        n += 1
    return palindrome

def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    values_out = []
    stack = Stack()
    n = 0
    for i in opstring:
        if i == "S":
            stack.push(values_in[n])
            n += 1
        elif i == "X":
            x =stack.pop()
            values_out.append(x)
            
    return values_out

# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    
    temp = Stack()
    lst = string.split()
    i = string[0]
    n = 0
    
    if m not in lst:
        return MIRRORED.NOT_MIRROR
    
    for i in lst:
        if not ((i in valid_chars) or (i == m)):
            return MIRRORED.INVALID_CHAR
        
    while i != m:
        temp.push(lst.pop())
        n += 1
        i = string[n]

