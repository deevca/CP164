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
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    st = set()
    stad = st.add
    values = [x for x in values if not (x in st or stad(x))]
    print(values)
    
def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    i = 0
    while i < len(string):
        if string[i:i+len(sub)] == sub:
            locations.append(i)
            i += len(sub)  
        else:
            i += 1
    return locations

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                leap_year = False
    else:
        leap_year = False
    return leap_year
    
def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    index = 0
    negative_index = -1
    while index <= range(int(len(string)/2)) and palindrome:
        if not (string[index].isalnum()):
            index += 1
        elif not (string[negative_index].isalnum()):
            negative_index -= 1
        elif string[index].lower() != string[negative_index].lower():
            palindrome = False
            index += 1
            negative_index -= 1
        else:
            index += 1
            negative_index -= 1
    return palindrome
    
def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    if name[0].isalpha()==False and name[0]!="_":
        valid = False
    else:
        for i in name:
            if i.isalnum() == False and i!="_":
                valid = False
    return valid
    
def median_scores(fv):
    """
    -------------------------------------------------------
    Determines the median of a series of integers in a file.
    Use: median = median_scores(fv)
    -------------------------------------------------------
    Parameters:
        fv - a file variable for an already open file of integers (file)
    Returns:
        median - the median of the values in the file (float)
    -------------------------------------------------------
    """
    for line in fv:
        try:
            score = int(line.strip())
            scores.append(score)
        except ValueError:
            print(f"Skipping invalid value: {line.strip()}")

    scores.sort()

    n = len(scores)
    if n % 2 == 0:
        middle1 = scores[n // 2 - 1]
        middle2 = scores[n // 2]
        median = (middle1 + middle2) / 2.0
    else:
        median = scores[n // 2]

    return median

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    for index_list1 in range(len(a[0])):
        temp_list = []
        for index_main_list in range(len(a)):
            temp_list.append(a[index_main_list][index_list1])
        b.append(temp_list)
    return b

    
def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = [[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k]*b[k][j]
    return c

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = [[0]*len(a) for i in range(len(a[0]))]
    for j in range(len(a)-1,-1,-1):
        for i in range(len(a[0])):
            b[i][j] = a[j][i]
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b