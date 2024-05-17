#!/usr/bin/env python3
"""
This module is implementing logic of adding matrices
"""


def add_matrices2D(mat1, mat2):
    """
    function add matrices that adds two matrices
    by adding two elements in the same position
    """
    if len(mat1) != len(mat2):
        return None
    result = []
    for arr in range(len(mat1)):
        if len(mat1[arr]) != len(mat2[arr]):
            return None
    innerArr = []
    for num in range(len(mat1[arr])):
        innerArr.append(mat1[arr][num] + mat2[arr][num])
        result.append(innerArr)

    return result
