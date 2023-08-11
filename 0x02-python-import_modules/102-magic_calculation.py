#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    """
    Match bytecode provided by Holberton School.

    This function performs a specific computation pattern based on the values of a and b.
    """
    if a < b:
        result = add(a, b)
        for i in range(4, 6):
            result = add(result, i)
        return result
    else:
        return sub(a, b)
