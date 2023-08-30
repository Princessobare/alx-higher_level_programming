#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a function that multiplies a matrix using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the result of multiplication of matrices.

    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    """

    return (np.matmul(m_a, m_b))
