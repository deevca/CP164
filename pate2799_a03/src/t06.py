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
from functions import reroute

values_in = [3, 4, 5, 6, 7, 8, 9, 10, 11]
opstring = "SSXXSXSSSSXX"

values_out = reroute(opstring, values_in)
print (f"Opstring: {opstring}")
print (f"Original list: {values_in}")
print (f"Reordered Version: {values_out}")