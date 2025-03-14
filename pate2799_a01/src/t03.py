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
from functions import is_leap_year

year = int(input("Enter a year to be checked: "))

leap_year = is_leap_year(year)

if leap_year == True:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))