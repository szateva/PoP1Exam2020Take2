# 13021326

""" Consider the function swap_min_max(L) that exchanges the positions of (in other
words, swaps) the maximal and the minimal numbers in a list L of integers. It re-
turns the result as a new list. If there are several numbers equal to the maximum, or
several numbers equal to the minimum, or both, swap the the last number equal to the
maximum with the last number equal to the minimum. You may assume that L has at
least two distinct numbers.
Write a pytest program with six test cases to check the correctness of swap_min_max.
(Note that you do NOT need to implement the function swap_min_max itself.) Diversity
of your tests is important in marking. """

import pytest

from implementation_file import *

# simple case, one min one max, all positive integers
def test_swap_min_max1():
    L = [1, 2, 3, 4, 5]
    assert swap_min_max(L) == [5, 2, 3, 4, 1]

# multiple mins
def test_swap_min_max2():
    L = [1, 2, 3, 1, 4, 5]
    assert swap_min_max(L) == [1, 2, 3, 5, 4, 1]

# multiple max
def test_swap_min_max3():
    L = [4, 3, 2, 5, 1, 5]
    assert swap_min_max(L) == [4, 3, 2, 5, 5, 1]

# negative values
def test_swap_min_max4():
    L = [9, 2, -4, 5, -1, 6]
    assert swap_min_max(L) == [-1, 2, -4, 5, 9, 6]

# mutliple min and multiple max
def test_swap_min_max5():
    L = [2, 3, 5, -2, 3, -2, 5]
    assert swap_min_max(L) == [2, 3, 5, -2, 3, 5, -2]

# all values are the same
def test_swap_min_max6():
    L = [0, 0, 0, 0]
    assert swap_min_max(L) == [0, 0, 0, 0]